from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Troque por uma chave secreta mais segura em produção

# Simulando um banco de dados temporário
users_db = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        hashed_password = generate_password_hash(password, method='sha256')
        users_db.append({'username': username, 'password': hashed_password})

        flash('Registro bem-sucedido! Faça login agora.')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = next((u for u in users_db if u['username'] == username), None)
        if user and check_password_hash(user['password'], password):
            flash('Login bem-sucedido!')
            return redirect(url_for('notes'))

        flash('Credenciais inválidas. Tente novamente.')

    return render_template('login.html')

@app.route('/notes')
def notes():
    return render_template('notes.html')

if __name__ == '__main__':
    app.run(debug=True)
