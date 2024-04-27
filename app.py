from flask import Flask, request
from helpers import lookup

# Configure application
app = Flask(__name__)


@app.route("/symbol", methods=["GET","POST"])
def get_data():
    symbol = request.args.get("symbol")
    return lookup(symbol)
