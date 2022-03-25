from flask import Flask, render_template, request # Flask is a application
# used to run/serve our application
# request is used to access the file which is uploaded by the user in out application
# render_template is used for rendering the html pages
import pickle # pickle is used for serializing and de-serializing Python object structures

app=Flask(__name__) # our flask app

@app.route('/') # rendering the html template
def home():
    return render_template('home.html')
@app.route('/predict') # rendering the html template
def index() :
    return render_template("index.html")

@app.route('/data_predict', methods=['POST']) # route for our prediction
def predict():
    at = request.form['at'] # requesting for at data
    v = request.form['v'] # requesting for v data
    ap = request.form['ap'] # requesting for ap data
    rh = request.form['rh'] # requesting for rh data
    
    # coverting data into float format
    data = [[float(at), float(v), float(ap), float(rh)]]
    
    # loading model which we saved
    model = pickle.load(open('CCPP.pkl', 'rb'))
    
    prediction= model.predict(data)[0]
    return render_template('predict.html', prediction=prediction)

if __name__ == '__main__':
    app.run()