from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/github', methods=['POST'])
def github_ldif_metrics():
    github_deployment_metrics = request.json
    return github_deployment_metrics
