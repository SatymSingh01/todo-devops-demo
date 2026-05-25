from flask import Flask, jsonify

app = Flask(__name__)

# Simple in-memory todo list
todos = [
    {"id": 1, "title": "Learn Kubernetes", "done": False},
    {"id": 2, "title": "Learn Helm", "done": False},
    {"id": 3, "title": "Learn Argo CD", "done": False},
]

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos), 200

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Todo API running",
        "endpoints": {
            "health": "/health",
            "todos": "/todos"
        }
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)