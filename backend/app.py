from flask import Flask



app = Flask(__name__)


@app.route('/me')
def me_test():
    

    return {
        "username": "faslu ",
        "theme": "dark",
        "image": "dop",
    }


@app.route('/users')
def users_api():
    return {
        "username": "faslu ",
        "theme": "dark",
        "image": "dop",
    }


if __name__ == "__main__":
    app.run(debug=True)