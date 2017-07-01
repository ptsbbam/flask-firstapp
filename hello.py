#imports Flask from the package flask
from flask import Flask

#Creates an instance of Flask object using our module's name as a parameter.
app = Flask(__name__)

#Python decorator. Means that the function directly below it should be called whenever a user visits the main root page of our web application ("/")
@app.route("/")

#Simple function that returns "Hello, World!" 
def index():
  return "Hello, World!"

#Python idiom that evaluates to true if the application is run directly. Prevents python scripts form being unintentionally run when they are imported into other Python files. 
if __name__ == '__main__':

  #starts the Flask's development server on our local machine. Port 5000 for local, 80 for production, set the debug to True which will help us see detailed errors directly on the web browser. 
  app.run(port=5000, debug = True) 
