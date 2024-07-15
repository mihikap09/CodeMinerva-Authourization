# app/app.py

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow Cross-Origin Requests

@app.route('/api/permission', methods=['POST'])
def permission():
    data = request.get_json()
    permission_granted = data.get('permission_granted')
    if permission_granted:
        # Handle permission granted (e.g., save to database)
        return jsonify({'message': 'Permission granted'}), 200
    else:
        return jsonify({'message': 'Permission denied'}), 400

if __name__ == '__main__':
    app.run(debug=True)
