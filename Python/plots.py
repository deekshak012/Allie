from flask import Flask,render_template,url_for,request,send_file, make_response
from flask_bootstrap import Bootstrap 
import pandas as pd
from datetime import datetime
import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import json
# import os
# template_dir = os.path.abspath('../templates')
# app = Flask(__name__, template_folder=template_dir)
app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
app.config.from_object(__name__)
Bootstrap(app)
#To load all values from CSV to variables
def loaderFunction(var):

        #read for CSV, make sure the name is a match as well
        df = csvFileToDataFrame()

        mainDates = df.loc[:,"Dates"]
        moodChoicesValues = df.loc[:,"Mood"]
        stressValues =  df.loc[:,"StressLevels"]
        cigsChoicesValues= df.loc[:,"Cigarette"]
        alcoholChoicesValues= df.loc[:,"Alcohol"]
        workHoursValues= df.loc[:,"WorkingHoursClocked"]
        workOutChoicesValues= df.loc[:,"WorkOut"]
        diary = df.loc[:,"Diary"]
        
        if var == "Dates":
          return mainDates

        elif var == "Mood":
          return moodChoicesValues
        
        elif var == "StressLevels": 
          return stressValues

        elif var == "Cigarette":
          return cigsChoicesValues

        elif var == "Alcohol":
          return alcoholChoicesValues

        elif var == "WorkingHoursClocked":
          return workHoursValues

        elif var == "WorkOut":
          return workOutChoicesValues

        elif var == "Diary":
          return diary
        
def csvFileToDataFrame():
  df = pd.read_csv('TableMain.csv')
  return df;        
        

#Variables to load it in, copy paste this directly
def getChartALLVariables(df):
  mainDates, moodChoicesValues, stressValues,
  foodValues, cigsChoicesValues, alcoholChoicesValues, 
  waterVales, sleepValues, workHoursValues,timeSpentSocialMediaValues, 
  workOutChoicesValues = loaderALLFunction(df)
  

#Function to get Chart for moodChoicesValues
@app.route('/mood')
def moodValuesChart():
  f = plt.figure()
  f.set_figwidth(8)
  f.set_figheight(5)
  mood = loaderFunction('Mood')
  plt.hist(mood,bins=6, rwidth=0.5)
  plt.xlabel('Mood')
  plt.ylabel('Number of Times in duration')
  plt.title('Mood Values')
  plt.savefig('Mood.png')
  return send_file('Mood.png',
                     mimetype='image/png')
  

#Function to get Chart for stressValues
@app.route('/stress')
def stressValuesChart():
  dates = loaderFunction('Dates')
  dates = dates[len(dates)-7:]
  stress = loaderFunction('StressLevels')
  stress = stress[len(stress)-7:]
  work = loaderFunction('WorkingHoursClocked')
  work = work[len(work)-7:]
  work = work/2
  fig, ax = plt.subplots()
  ax2 = ax.twinx()
  fig.set_figwidth(8)
  fig.set_figheight(5)
  ax.plot(dates, stress, color = 'g')
  ax2.plot(dates, work, color = 'b')
  ax.set_xlabel('Dates', color = 'r')
  ax.set_ylabel('Stress', color = 'g')
  ax2.set_ylabel('Work Hours', color = 'b')
  plt.savefig('Stress.png')
  return send_file('Stress.png',
                     mimetype='image/png')
  

#Function to get Chart for foodChoicesValues
def foodValuesChart():
  food = loaderFunction('FoodTypeConsumption')
  plt.hist(food)
  plt.xlabel('Food Type Consumption')
  plt.ylabel('Number of Times in duration')
  plt.title('Food Values')
  plt.savefig('Food.png')
  plt.show()
  


#Function to get Chart for cigValuesChart
def cigValuesChart():
  cig = loaderFunction('Cigarette')
  plt.hist(cig)
  plt.xlabel('Cigarette Consumption Type')
  plt.ylabel('Number of Times in duration')
  plt.title('Cigarette Values')
  plt.savefig('Cig.png')
  plt.show()
  

#Function to get Chart for AlcoholValuesChart
def AlcoholValuesChart():
  alc = loaderFunction('Alcohol')
  plt.hist(alc)
  plt.xlabel('Alcohol Consumption Type')
  plt.ylabel('Number of Times in duration')
  plt.title('Alcohol Values')
  plt.savefig('Alcohol.png')
  plt.show()
  

#Function to get Chart for waterValues
def waterValuesChart():
  dates = loaderFunction('Dates')
  water = loaderFunction('WaterConsumption')
  plt.bar(dates, water)
  plt.xlabel('Dates')
  plt.ylabel('Water Consumptions Levels')
  plt.title('Water Consumptions Levels chart')
  plt.savefig('Water.png')
  plt.show()
  

#Function to get Chart for sleepValues
def sleepValuesChart():
  dates = loaderFunction('Dates')
  sleep = loaderFunction('SleepingHours')
  plt.bar(dates, sleep)
  plt.xlabel('Dates')
  plt.ylabel('Number of Hours Slept')
  plt.title('Number of Hours Slept Over duration')
  plt.savefig('Sleep.png')
  plt.show()
  

  

#Function to get Chart for workValues
def workValuesChart():
  dates = loaderFunction('Dates')
  work = loaderFunction('WorkingHoursClocked')
  plt.bar(dates, work)
  plt.xlabel('Dates')
  plt.ylabel('Working Hours Clocked')
  plt.title('Number of Hours Clocked at Work Over duration')
  plt.savefig('WorkHours.png')
  plt.show()
  

#Function to get Chart for socialValues
def socialValuesChart():
  dates = loaderFunction('Dates')
  social = loaderFunction('TimeSpentSocialMedia')
  plt.bar(dates, social)
  plt.xlabel('Dates')
  plt.ylabel('Time Spent on Social Media')
  plt.title('Number of Hours Spent on Social Media')
  plt.savefig('Social.png')
  plt.show()
  

#Function to get Chart for workoutValuesChart
@app.route('/workout')
def workoutValuesChart():
  work = loaderFunction('WorkOut')
  work=work[len(work)-7:]
  work = work*2
  dates = loaderFunction('Dates')
  dates=dates[len(dates)-7:]
  stress = loaderFunction('StressLevels')
  stress=stress[len(stress)-7:]
  fig, ax = plt.subplots()
  fig.set_figwidth(8)
  fig.set_figheight(5)
  ax2 = ax.twinx()
  ax.plot(dates, stress, color = 'g')
  ax2.plot(dates, work, color = 'b')
  ax.set_xlabel('Dates', color = 'r')
  ax.set_ylabel('Stress', color = 'g')
  ax2.set_ylabel('Workout Time', color = 'b')
  plt.savefig('workout.png')
  plt.legend()
  return send_file('workout.png',
                     mimetype='image/png')

@app.route('/diary')
def diary():
  dates = loaderFunction('Dates')
  diary = loaderFunction('Diary')
  arr=[]
  for i,date in enumerate(dates):
    ht={}
    ht['date'] = date
    ht['dairy']= diary[i]
    arr.append(ht)
  response = make_response(json.dumps(arr), 200)
  response.mimetype = "text/plain"
  response.headers['Access-Control-Allow-Origin'] = '*'
  return response

@app.route('/userdata', methods=['POST'])
def userdata():
    today = '12/07/2021'
    mood = request.form['mood']
    stress = request.form['stress']
    work = request.form['work']
    excercise = request.form['excercise']
    alcohol = request.form['alcohol']
    cig = request.form['cig']
    diary = request.form['diary']  
    df = pd.DataFrame({'Date':[today],
                    'Mood': [mood],
                   'StressLevels': [stress],
                   'Cigarette': [cig],
                   'Alcohol': [alcohol],
                   'WorkingHoursClocked': [work],
                   'WorkOut':[excercise],
                   'Diary':[diary]})
    df.to_csv('TableMain.csv', mode='a', index=False, header=False)
    return "Added successfully"
    
    