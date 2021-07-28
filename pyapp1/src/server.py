from flask import Flask
import os 

server = Flask(__name__)

@server.route("/app1")

def hello():
    return "Hello World from App1!"

if __name__ == "__main__":
   server.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 5001)))