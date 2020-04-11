from flask import Flask, request

app = Flask(__name__)

@app.route('/json', methods=['POST'])
def handleJson():
    req_data = request.get_json()
    return ''
