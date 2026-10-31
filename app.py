
from flask import Flask, request, jsonify, render_code

app = Flask(__name__)

# The password is hidden safely on the server
CORRECT_PASSWORD = "SuperSecretPassword123"

@app.route('/')
def home():
    # Serves your HTML file to the user
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user_password = data.get('password')
    
    # The comparison happens here, completely hidden from the browser
    if user_password == CORRECT_PASSWORD:
        return jsonify({"status": "success", "message": "Access Granted!"})
    else:
        return jsonify({"status": "error", "message": "Incorrect Password!"}), 401

if __name__ == '__main__':
    app.run(debug=True)
