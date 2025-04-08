from flask import Flask, request, jsonify
import requests
import base64

app = Flask(__name__)

# Base64 Encoded Webhook URLs
encoded_source_webhook = 'aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTM1OTE1NDYwNzQwMTU5ODk4Ni9aME9qX2IwVGw1VVJLRkpxMnJpMm5tRjNNMFo0Z21ldmFvSyZjc3FvSUpMamhmLUxCZVJxYi1UemZ0UXF3Y0NISU5VeGqG8W3cmF0_0z6-V45Tt1mT3g2KYhfr'
encoded_target_webhook = 'aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTM1OTI0ODgwNTUyMTkxNjE3NS8yUFJwV21SYjN1d3hYZWhxUVYxQnhsOEUzMkYwyL5RpdnDBKQUcIzZY7u6FgPlYlJdbqp'

# Decode the Base64 encoded URLs
source_webhook_url = base64.b64decode(encoded_source_webhook).decode()
target_webhook_url = base64.b64decode(encoded_target_webhook).decode()

@app.route('/receive-webhook', methods=['POST'])
def receive_webhook():
    try:
        # Get the incoming webhook data (in JSON format)
        data = request.json
        print("Received webhook data:", data)

        # Forward the received data to the target Discord webhook
        response = requests.post(target_webhook_url, json=data)

        # Check if the forwarding request was successful
        if response.status_code == 204:
            return jsonify({'status': 'success', 'message': 'Webhook forwarded successfully'}), 200
        else:
            return jsonify({'status': 'error', 'message': 'Failed to forward webhook'}), 500
    except Exception as e:
        print(f"Error forwarding webhook: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


if __name__ == '__main__':
    # Start the Flask server on port 5000 (default)
    app.run(host='0.0.0.0', port=5000)
