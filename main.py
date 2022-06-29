from flask import Flask, render_template, url_for, request, app

#creamos un objeto (variable)de la clase Flask en poo era una instancia o copia
app = Flask(__name__)

#creamos un condicional para convertir este archivo como el principal
#para la ejecución del proyecto
@app.route("/", methods=['GET', 'POST'])
def inicio():
    return render_template("index2.html")

@app.route("/post_mesg", methods=["POST"])
def enviar_datos():
    if request.method == "POST":
        mensaje = request.form["msg"]
        mensaje1 = request.form["msg1"]
        return mensaje + "<br>" + mensaje1
@app.route("/index", methods=['GET', 'POST'])
def index():
    return render_template("index.html")

    app.run(host="0.0.0.0", port="5000", debug=True)

