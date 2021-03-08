from flask import Flask, render_template, request, redirect
import random

app = Flask(__name__)

@app.route("/")
def input():
    return render_template("input.html")

@app.route("/answer", methods=["post"])
def answer():
    name = request.form["inputname"]
    try:
        new_name = random.choice(name)
        return render_template("answer_named.html",
                               name = name,
                               new_name = new_name)
    except Exception as e:
        return render_template("answer_noname.html",
                               error = e)

if __name__ == "__main__":
    app.run(debug=True)