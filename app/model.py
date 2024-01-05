import pandas as pd # to import csv and for data manipulation
import seaborn as sns # for intractve graphs
import numpy as np # for linear algebra
import warnings
import os
from sklearn.impute import SimpleImputer
import pickle
#from pytorch_tabnet.tab_model import TabNetClassifier
#import torch
import tensorflow as tf
from tensorflow.keras.models import load_model
warnings.filterwarnings('ignore')

class prediction(object):

        
    def mlpclassifier(self):
    #class_weight = dict({2:1, 1:15, 0:50})

        nnmodel = load_model('newnnmodel.h5')

        return nnmodel


    def defaultClassifier(self):
        return self.mlpclassifier()

    def predictResult(self, data):
        inputData = []
        for col in self.cols:
            inputData.append(data[col])

        inputData = {'0' : inputData}
        test = pd.DataFrame.from_dict(inputData, orient='index', columns=self.cols)
        test= test.to_numpy(dtype = 'float')
        print(test)
        test = test.reshape(1,-1)
        pred = self.model.predict(test)
        new_prediction = np.round(pred).astype(int)
        print(new_prediction)

        if new_prediction[0] == 0:
            return "Non Fatal Accident"
        elif new_prediction[0] == 1:
            return "Fatal Accident"
            
        return "None"

    def __init__(self):
        
        self.cols = ['Latitude', 'Longitude','Number_of_Casualties', 'Number_of_Vehicles','Road_Type', 'Speed_limit', 'Light_Conditions', 'Weather_Conditions',
       'Road_Surface_Conditions', 'Carriageway_Hazards', 'Junction_Control',
       'Pedestrian_Crossing-Human_Control','Pedestrian_Crossing-Physical_Facilities', 'Special_Conditions_at_Site',
       'Urban_or_Rural_Area']
        self.total = self.cols + ['Accident_Severity']
     
        self.model = self.defaultClassifier()

# init()

