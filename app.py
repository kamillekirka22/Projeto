from flask import Flask, render_template, request 
app = Flask(__name__)

usuario_valido={
    "email": "teste@gmail.com",
    "senha": "123456"
}

@app.route('/', methods=[ "GET", "POST"])
def login():
    mensagem =""

    if request.method == "POST":
        email = request.form("email")
        senha = request.form("senha")

        if email == usuario_valido["email"] and senha == usuario_valido["senha"]:
            mensagem = "Login realizado com sucesso!"
        else:
            mensagem == "Email ou senha incorretos. Tente novamente."

    return render_template("login.html", mensagem=mensagem)

if __name__ == "__main__":
    app.run(debug=True)