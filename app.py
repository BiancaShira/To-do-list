from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
              return render_template("index.html")

@app.route("/daily")
def daily():
        daily_to_do = open("daily.txt")
        return render_template("daily.html" ,  daily_to_do = daily_to_do)

@app.route("/weekly")
def weekly():
        weekly_to_do = open("weekly.txt")
        return render_template("weekly.html" ,  weekly_to_do = weekly_to_do)

@app.route("/monthly")
def monthly():
        monthly_to_do = open("monthly.txt")
        return render_template("monthly.html" ,  monthly_to_do = monthly_to_do)