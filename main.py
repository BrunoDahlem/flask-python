from flask import Flask, render_template

app = Flask(__name__)

# 1º pagina do site

# Route

# Função
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


@app.route('/users/<user>')
def users(user):
    d = {
        "name":"bruno",
        "idade":20
        }
    return render_template('users.html',d=d)
# Site no ar
if __name__ == '__main__':
    app.run(debug=True)