from flask import Flask

#  __name__ is a convenient way to get the import name of the place the app is defined.
# Flask uses the import name to know where to look up resources, templates, static files, instance folder, etc
application = Flask(__name__)

@application.route("/")
def home():
    return "Hello CloudSkills!"

@application.route("/hello")  #http://127.0.0.1:5000/hello shows goodbye!
def goodbye():
    return "Goodbye!"

application.run(host='127.0.0.1', port='5000')  #Specify host and port when running locally, otherwise leave as ()