from flask import Flask, render_template

# Initialize Flask app
app = Flask(__name__, template_folder="templates")

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# Run app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
