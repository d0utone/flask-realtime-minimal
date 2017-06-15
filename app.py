# python (flask) side:
import time
from flask import Response, Flask

app = Flask(__name__)

@app.route('/event_stream')
def stream():
    def event_stream():
        i = 0
        while True:
            time.sleep(3)
            i += 1
            yield 'data: %s\n\n' % i

    return Response(event_stream(), mimetype="text/event-stream")

@app.route('/')
def index():
    return '''
    <span id="container"></h1>Lets Go</h1></span>
    <script>
      var source = new EventSource('/event_stream');
      source.onmessage = function(event){
        document.getElementById('container').append(event.data)

      };
    </script>
    '''

if __name__ == '__main__':
    app.run(debug=True)
