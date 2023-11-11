from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('your-html-filename.html')

@socketio.on('input')
def handle_input(input_text):
    import subprocess
    output = subprocess.getoutput(input_text)
    socketio.emit('output', output)

if __name__ == '__main__':
    socketio.run(app)
