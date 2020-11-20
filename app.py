from flask import Flask, send_from_directory

app = Flask(__name__)


@app.route('/<path:path>', methods=['GET'])
def serve_path(path):
    return send_from_directory('static', path)


@app.route('/')
def serve_root():
    return send_from_directory('static', 'index.html')


if __name__ == "__main__":
    app.run()
