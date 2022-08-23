from flask import Flask
app = Flask(__name__)

# config
app.config['DEBUG'] = True


@app.route('/')
def hello_world():
    return 'Hello to the World of Flask add debug!'


if __name__ == '__main__':
    app.run()
