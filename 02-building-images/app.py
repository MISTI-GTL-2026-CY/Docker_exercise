from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    name = os.environ.get('NAME', 'World')
    return f'''
    <html>
        <head><title>Docker Exercise</title></head>
        <body>
            <h1>Hello, {name}!</h1>
            <p>Congratulations! You've successfully built and run your first Docker container.</p>
            <p>This Flask application is running inside a Docker container that you built yourself!</p>
        </body>
    </html>
    '''

if __name__ == '__main__':
    # Note: debug=False is recommended for production use
    # For learning purposes, you can set debug=True to see detailed error messages
    app.run(host='0.0.0.0', port=5000, debug=False)
