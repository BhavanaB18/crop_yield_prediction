from Crop_Yield_prediction_Model import predict_yield as py, final_model
import numpy as np
from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        form = request.form
        area = float(form['area'])
        item = int(form['item'])
        year = int(form['year'])
        rainfall = float(form['rainfall'])
        #  gender = form['gender']
        pesticides = float(form['pesticides'])
        temp = float(form['temp'])
        p = []
        p += [area, item, year, rainfall, pesticides, temp]
        # if gender == "M":
        #     p+=[1]
        # else:
        #     p+=[0]
        # if pclass == 2:
        #     p+=[1,0]
        # elif pclass == 3:
        #     p+=[0,1]
        # else:
        #     p+=[0,0]
        # if place.lower() == "queenstown":
        #     p+=[1,0]
        # elif place.lower() == "southampton":
        #     p+=[0,1]
        # else:
        #     p+=[0,0]

        # param_config = {
        #     "Area": [0],
        #     "Item": [1],
        #     "Year": [0],
        #     "average_rain_fall_mm_per_year": [1485.0],
        #     'pesticides_tonnes': [121.00],
        #     'avg_temp': [16.37]
        # }
        result = py([p], final_model)
        return render_template('index.html', res=str(result))
    # return res

    return render_template('index.html', res="Fill the details and Click Submit")


app.run()
