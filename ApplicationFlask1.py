# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 12:23:43 2021

@author: ssatyakam
"""

from flask import Flask
from flask import jsonify as jf
from flask import request
import simplejson as sjson
import watchdog as wd


json101 = "redcap_url=https%3A%2F%2Fredcap.uchicago.edu%2F&project_url=https%3A%2F%2Fredcap.uchicago.edu%2Fredcap_v9.5.36%2Findex.php%3Fpid%3D10399&project_id=10399&username=ssatyakam&record=1&instrument=demographics&demographics_complete=0"

app = Flask(__name__)

@app.route('/')
def hello():
    return "Service API For Data Standardisation GEN online"

@app.route('/datastandardisation/', methods=['POST'])                                                                                                    
def datastandardisation():                                                                                                                              
    if request.method == 'POST':
        #if re:
            
            #return log_the_user_in(request.form['username'])
        #else:
            #error = 'Invalid username/password'
    data = request.form
    print(data)
    
    # ... do your business logic, and return some response
    # e.g. below we're just echo-ing back the received JSON data
    return jf(data)

if __name__=="__main__":
    app.run()


