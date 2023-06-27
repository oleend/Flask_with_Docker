from flask import Flask, jsonify, render_template, redirect

print(__name__ + 'Current Exicution')

app = Flask(__name__)

@app.route('/flask-api')
def hello():
    return jsonify(message='Hello, Flask API!')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/redirect')
def redirect_to_flask_api():
    return redirect('/flask-api')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')