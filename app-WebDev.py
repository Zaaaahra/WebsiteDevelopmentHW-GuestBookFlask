from flask import Flask, render_template, request, session, redirect
from datetime import datetime

app = Flask(__name__)
app.secret_key = "dev-secret"  # In production, use a secure key

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/sign", methods=["GET", "POST"])
def sign():
    if request.method == "POST":
        name = request.form["name"]
        entry = {"name": name, "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        guestbook = session.get("guestbook", [])
        guestbook.insert(0, entry)  # Insert at beginning to show latest first
        session["guestbook"] = guestbook
        return redirect("/guestbook")
    return render_template("sign.html")

@app.route("/guestbook")
def guestbook():
    guestbook = session.get("guestbook", [])
    return render_template("guestbook.html", guestbook=guestbook)

@app.route("/clear")
def clear():
    session["guestbook"] = []
    return redirect("/guestbook")

if __name__ == "__main__":
    app.run(debug=True)
