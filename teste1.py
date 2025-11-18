from flask import Flask, render_template, request
app = Flask (__name__)

historico_registros = []

@app.route("/")
def index():
    return render_template("index.html.") 

@app.route("/resultado", methods=['POST'])
def resultado():
    nome = request.form.get('nome')
    nascimento = request.form.get ('nascimento')
    sexo = request.form.get ('sexo')
    email = request.form.get ('email')
    humor = request.form.get('humor')
    anotacoes = request.form.get('anotacoes')
    data = request.form.get('data')

    novo_registro = {"nome": nome, 
                     "data": data, 
                     "humor": humor, 
                     "anotacoes": anotacoes
                     }
    historico_registros.append(novo_registro)
    
    return render_template("resultado.html", nome=nome, humor=humor, anotacoes=anotacoes, data=data, nascimento=nascimento, sexo=sexo, email=email,)
@app.route('/historico')
def historicos():
    return render_template('historico.html', registros=historico_registros)

if __name__ == "__main__":
    app.run(debug=True)
    



