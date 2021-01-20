from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
app = Flask(__name__)
model = pickle.load(open('storm_model.pkl','rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/classify", methods=['POST'])
def classify():
    if request.method == 'POST':
        season = int(request.form['season'])
        stages = int(request.form['stages'])
        ridges = int(request.form['ridges'])
        mjo = int(request.form['mjo'])
        sea_temp = int(request.form['sea_temp'])
        shear = int(request.form['shear'])

        predictions = int(model.predict([[season,stages,sea_temp,ridges,shear,mjo]]))

        direction = ""
        if(predictions==0):
            direction="West - NorthWest"
        elif(predictions==1):
            direction="West - SouthWest"
        elif(prediction==2):
            direction="NorthWest"
        elif(predictions==3):
            direction="West"
        elif(predictions==4):
            direction="North"

        return render_template('index.html',prediction_text=direction)

    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

