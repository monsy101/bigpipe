from flask import Flask, render_template, stream_with_context, Response
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index_no_js.html')

@app.route('/content')
def get_content():
    def generate():
        yield "This is the main content of the page.\n"
        time.sleep(3)  # Simulating a 3-second delay
        yield "This content was loaded asynchronously!\n"

    return Response(stream_with_context(generate()), content_type='text/plain; charset=utf-8')

if __name__ == "__main__":
    app.run(debug=True)
