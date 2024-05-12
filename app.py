from flask import Flask, render_template, request
import numpy as np
import pickle


app = Flask(__name__,template_folder='template')
model = pickle.load(open('predictor.pickle', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        gender = request.form['gender']
        if gender == 'Female':
            gender_Female = 1
        else:
            gender_Female = 0

        ever_married = request.form['ever_married']
        if ever_married == '1':
            ever_married = 1
        else:
            ever_married = 0

        Residence_type = request.form['Residence_type']
        if Residence_type == '1':
            Residence_type = 1
        else:
            Residence_type = 0


        age = float(request.form['age'])
        hypertension = request.form.getlist('hypertension')
        heart_disease =request.form.getlist('heart_disease')
        avg_glucose_level = float(request.form['avg_glucose_level'])
        bmi = float(request.form['bmi'])


        work_type = request.form['work_type']

        if work_type == 'Private':
            work_type_Private = 1
            work_type_Self_employed = 0
            work_type_children = 0
            work_type_Govt_job = 0

        elif work_type == "Self_employed":
            work_type_Private = 0
            work_type_Self_employed = 1
            work_type_children = 0
            work_type_Govt_job = 0

        elif work_type == "children":
            work_type_Private = 0
            work_type_Self_employed = 0
            work_type_children = 1
            work_type_Govt_job = 0

        else:
            work_type_Private = 0
            work_type_Self_employed = 0
            work_type_children = 0
            work_type_Govt_job = 1


        smoking_status = request.form['smoking_status']

        if smoking_status == "formerly_smoked":
            smoking_status_formerly_smoked = 1
            smoking_status_never_smoked = 0
            smoking_status_Smokes = 0
            smoking_status_Unknown  = 0

        elif smoking_status == "never_smoked":
            smoking_status_formerly_smoked = 0
            smoking_status_never_smoked = 1
            smoking_status_Smokes = 0
            smoking_status_Unknown  = 0

        elif smoking_status == "Smokes":
            smoking_status_formerly_smoked = 0
            smoking_status_never_smoked = 0
            smoking_status_Smokes = 1
            smoking_status_Unknown  = 0

        else:
            smoking_status_formerly_smoked = 0
            smoking_status_never_smoked = 0
            smoking_status_Smokes = 0
            smoking_status_Unknown = 1


        values = [np.array([[gender_Female,age, hypertension, heart_disease, ever_married, Residence_type, avg_glucose_level, bmi, work_type_Govt_job, work_type_Private,work_type_Self_employed, work_type_children, smoking_status_Unknown, smoking_status_formerly_smoked, smoking_status_never_smoked, smoking_status_Smokes]],dtype=object)]
        print(values)
        prediction = model.predict(values)

        return render_template('result.html', prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)

