from flaskr import app


@app.route('/Hello')
def hello():
    return 'Hello world!'