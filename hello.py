from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')

def index():
	first_name = "Khalid"
	return render_template("index.html", first_name=first_name)

#localhost:5000/user/khalid
@app.route("/user/<name>")

def user(name):
	return render_template("user.html", user_name=name)

#create error pages

#invalid url 404

@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404


#internal server error 500
@app.errorhandler(500)
def page_not_found(e):
	return render_template("500.html"), 500
