from flask import Flask, render_template,redirect, url_for


app = Flask(_name_)
L
@app.route('/')
def index() :
   return render_template("login.html")


@app.route('/new')
def new_user():
   return render_template("register.html")


@app.route('/profile')
def profile():
   return render_template('profile.html')


if _name_ == '_main_'
   app.run(debug=True)
