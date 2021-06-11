from flask import Flask, request, render_template
import json
import os
app = Flask(__name__,template_folder='templates')
m=open('peoplejson.json',"r+")
entry =json.load(m)


@app.route('/')
def home():
   return render_template('home.html')



@app.route('/lis',methods=['POST','GET'])
def lis():
    l= str(request.form['values'])
    val = str(request.form['va'])
    print(l)
    dee=[]
    if(l=="name"):
        for a in entry:
            ram=[]
            if(a==val):
                print(a)
                ram.append(a)
                ram.append(entry[a]['Picture'])
                dee.append(ram)
            else:
                pass
        print(dee)
        return render_template("list1.html",rows = dee)
    elif(l=="state"):
        for a in entry:
            ram=[]
            if(entry[a]['State']==val):
                ram.append(a)
                ram.append(entry[a]['State'])
                ram.append(entry[a]['Salary'])
                ram.append(entry[a]['Grade'])
                ram.append(entry[a]['Room'])
                ram.append(entry[a]['Telnum'])
                ram.append(entry[a]['Picture'])
                ram.append(entry[a]['Keywords'])
                dee.append(ram)

    elif(l=="room"):
        for a in entry:
            ram=[]
            if(entry[a]['Room']==int(val)):
                ram.append(a)
                ram.append(entry[a]['State'])
                ram.append(entry[a]['Salary'])
                ram.append(entry[a]['Grade'])
                ram.append(entry[a]['Room'])
                ram.append(entry[a]['Telnum'])
                ram.append(entry[a]['Picture'])
                ram.append(entry[a]['Keywords'])
                dee.append(ram)
    print (dee)
    return render_template("lis.html",rows = dee)

@app.route('/list1',methods=['POST','GET'])
def list1():
    valuenum = str(request.form['valuesNum'])
    valuenum1 = int(request.form['valuenum1'])
    valuenum2 = int(request.form['valuenum2'])
    print(valuenum)
    dee=[]
    if(valuenum=="grade"):
        for a in entry:
            ram=[]
            print(type(entry[a]['Grade']),type(int(valuenum2)))
            if(entry[a]['Grade']!="" and entry[a]['Grade']<int(valuenum2) and entry[a]['Grade']>int(valuenum1)):
                ram.append(a)
                ram.append(entry[a]['State'])
                ram.append(entry[a]['Salary'])
                ram.append(entry[a]['Grade'])
                ram.append(entry[a]['Room'])
                ram.append(entry[a]['Telnum'])
                ram.append(entry[a]['Picture'])
                ram.append(entry[a]['Keywords'])
                dee.append(ram)

        return render_template("lis.html",rows = dee)
    elif(valuenum=="salary"):
        for a in entry:
            ram=[]
            if(entry[a]['Salary']!="" and entry[a]['Salary']<int(valuenum2) and entry[a]['Salary']>int(valuenum1)):
                ram.append(entry[a]['Picture'])
                dee.append(ram)
    return render_template("list2.html",rows = dee)


@app.route('/deleterecord', methods=['POST','GET'])
def deleterecord():
    value = request.form['valuesDEL']
    val1 = request.form['valueDEL']
    if(value=="nameDEL"):
        for a in entry.copy():
            if(a==val1):
                del entry[a]

    dee=[]
    for a in entry.copy():
        ram=[]
        ram.append(a)
        ram.append(entry[a]['State'])
        ram.append(entry[a]['Salary'])
        ram.append(entry[a]['Grade'])
        ram.append(entry[a]['Room'])
        ram.append(entry[a]['Telnum'])
        ram.append(entry[a]['Picture'])
        ram.append(entry[a]['Keywords'])
        dee.append(ram)
    return render_template('lis.html',rows=dee)


@app.route('/update',methods=['POST','GET'])
def update():
    value1 = str(request.form['ADD1'])
    value2 = str(request.form['ADD2'])
    value3 = str(request.form['val2'])

    if(value3=="key2"):
        for a in entry:
            if(a==value1):
                entry[a]['Keywords']=value2
    if(value3=="image2"):
        for a in entry:
            if(a==value1):
                entry[a]['Picture']=value2
    dee=[]
    for a in entry.copy():
        ram=[]
        ram.append(a)
        ram.append(entry[a]['State'])
        ram.append(entry[a]['Salary'])
        ram.append(entry[a]['Grade'])
        ram.append(entry[a]['Room'])
        ram.append(entry[a]['Telnum'])
        ram.append(entry[a]['Picture'])
        ram.append(entry[a]['Keywords'])
        dee.append(ram)	
    return render_template('lis.html',rows=dee)
if __name__ == '__main__':
    app.run( )