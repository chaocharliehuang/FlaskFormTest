from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users/<username>')
def show_user_profile(username):
    return render_template('user.html', username = username)

@app.route('/users', methods=['POST'])
def create_user():
    name = request.form['name']
    email = request.form['email']
    print name, email
    return redirect('/')

app.run(debug=True)