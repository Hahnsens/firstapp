from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
	return "fucks!"
if __name__ == '__main__':
	app.run(port=5000, debug=True)
