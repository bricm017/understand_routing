from flask import Flask #this allows flask to create the app

app = Flask(__name__) #creating an instance of Flask calss (app)

@app.route('/') # "@" associates the route to the function that follows
def hello_world(): 
    return 'Hello World' # Returns 'Hello World!' as a response

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/dino')
def dino():
    return "Hi Dino!"

@app.route('/repeat/20/TRex')
def TRex():
    return "TRex" init("20")

if __name__ == "__main__": # Ensure this file is being run directly and not from a different module  
    app.run(debug=True) # Run the app in debug mode.