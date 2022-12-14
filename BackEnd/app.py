from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres"
db = SQLAlchemy(app)


if __name__ == "__main__":
    app.run(debug=True)

@app.route("/")
def home():
    return "home"
