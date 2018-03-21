from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
from piapp.database import db_session

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/createRecord', methods=['GET', 'POST'])
def createRecord():
    if request.method == 'POST':
        for k, v in request.form.items():
            print(k, " -> ", v)
        return crearRegistro()
    else:
        return render_template('createRecord.html')

#practicing ajax
@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
app = Flask(__name__)

def crearRegistro():
    return "okaeri"
