from flask import Flask, render_template, request

app = Flask(__name__)

# Lista de perguntas
perguntas = [
    {
        "pergunta": "Em quantos dias Deus criou tudo e em qual dia ele descansou?",
        "opcoes": ["Em 3 dias e descansou no 4º", "Em 5 dias e descansou no 6º", "Em 6 dias e descansou no 7º", "Em 7 dias e descansou no 8º"],
        "correta": "Em 6 dias e descansou no 7º"
    },
    {
        "pergunta": "Em qual dia Deus criou o homem?",
        "opcoes": ["No primeiro dia", "No terceiro dia", "No sexto dia", "No sétimo dia"],
        "correta": "No sexto dia"
    },
    {
        "pergunta": "Qual animal enganou Eva?",
        "opcoes": ["Leão", "Serpente", "Corvo", "Cordeiro"],
        "correta": "Serpente"
    },
    {
        "pergunta": "Quais eram os nomes dos primeiros dois filhos de Adão e Eva?",
        "opcoes": ["Abraão e Moisés", "Caim e Abel", "Jacó e Esaú", "Pedro e João"],
        "correta": "Caim e Abel"
    },
    {
        "pergunta": "Quem matou Abel?",
        "opcoes": ["Caim", "Adão", "Moisés", "Ninguém"],
        "correta": "Caim"
    },
    {
        "pergunta": "Qual material Deus usou para formar Adão?",
        "opcoes": ["Água", "Areia", "Barro", "Pó da terra"],
        "correta": "Pó da terra"
    },
    {
        "pergunta": "Com que material Deus formou Eva?",
        "opcoes": ["Costela de Adão", "Barro", "Terra", "Folha"],
        "correta": "Costela de Adão"
    },
    {
        "pergunta": "Quem deu nome aos animais?",
        "opcoes": ["Eva", "Moisés", "Adão", "Deus"],
        "correta": "Adão"
    },
    {
        "pergunta": "Qual animal Deus usou para fazer roupas para Adão e Eva?",
        "opcoes": ["Serpente", "Leão", "Cordeiro", "Camelo"],
        "correta": "Cordeiro"
    },
    {
        "pergunta": "Qual era o animal mais esperto do Éden?",
        "opcoes": ["Águia", "Cão", "Serpente", "Cavalo"],
        "correta": "Serpente"
    }
]

@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/jogo")
def jogo():
    return render_template("index.html", pergunta_atual=0, score=0, perguntas=perguntas, numero_pergunta=1)

@app.route("/responder", methods=["POST"])
def responder():
    pergunta_atual = int(request.form["pergunta_atual"])
    resposta = request.form["resposta"]
    score = int(request.form["score"])

    if resposta == perguntas[pergunta_atual]["correta"]:
        score += 1

    pergunta_atual += 1

    if pergunta_atual >= len(perguntas):
        return render_template("final.html", score=score)

    return render_template(
        "index.html",
        pergunta_atual=pergunta_atual,
        score=score,
        perguntas=perguntas,
        numero_pergunta=pergunta_atual + 1
    )

if __name__ == "__main__":
    import os

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)


