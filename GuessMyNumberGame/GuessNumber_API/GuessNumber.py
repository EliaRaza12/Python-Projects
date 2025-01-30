from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # Allow frontend requests

secret_num = random.randint(1, 99)

@app.route('/guess', methods=['POST'])
def guess_number():
    global secret_num
    data = request.json
    guess = int(data.get('guess', 0))

    if guess < secret_num:
        return jsonify({"message": "Too low! Guess again."})
    elif guess > secret_num:
        return jsonify({"message": "Too high! Guess again."})
    else:
        secret_num = random.randint(1, 99)
        return jsonify({"message": f"Congrats! The number was {guess}. New number generated!"})

if __name__ == '__main__':
    app.run(debug=True)
