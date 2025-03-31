from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/flip', methods=['GET'])
def quantum_flip():
    result = "Heads" if random.random() < 0.5 else "Tails"
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
