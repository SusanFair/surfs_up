# Import dependencies
from flask import Flask

# Create a new flask app instance
app = Flask(__name__)

# Create Flask Routes
@app.route('/')
def hello_world():
    return 'Hello world'



# Run Flask App
# Mac: set FLASK_APP=app.py
# Windows: in Anaconda window run set FLASK_APP=app.py and flask run
# from the command line

# Create a new route???
#@app.route('/')
#def Photos():
#    return 'Photos'
