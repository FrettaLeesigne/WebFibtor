
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, redirect, request, url_for

from flask.ext.sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("fibtor.html", comments=Comment.query.all())

    comment = Comment(content=request.form["contents"])
    fibtor.session.add(comment)
    fibtor.session.commit()
    return redirect(url_for('index'))


# Connect to the Fibtor service

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="xiurobert",
    password="fibtorisgay",
    hostname="xiurobert.mysql.pythonanywhere-services.com",
    databasename="xiurobert$fibtor_gay",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299


fibtor = SQLAlchemy(app)

class Comment(fibtor.Model):

    __tablename__ = "fibtor"

    id = fibtor.Column(fibtor.Integer, primary_key=True)
    content = fibtor.Column(fibtor.String(4096))

