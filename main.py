from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Bem Vindo'

app.run(host='0.0.0.0')