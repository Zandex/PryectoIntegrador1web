import requests
from flask import Flask,request,render_template


app= Flask(__name__,template_folder='public')


actividades_list=['Agricultura','Comercio','Investigacion','Insumos','Transporte']

@app.route('/formulario',methods= ['GET'])
def sensorcreator():
    return render_template("forum_people.html",variables=actividades_list)

@app.route('/registro',methods= ['GET'])
def listparticipantes():
    participantes_list=requests.get('https://api-evergreen-289.azurewebsites.net/getpeople').json()
    return render_template("listregister.html",list=participantes_list)

@app.route('/savepeolple',methods =['POST'])
def guardarparticipante():
    people = dict(request.values)
    people['estrato']=int(people['estrato'])
    requests.post('https://api-evergreen-289.azurewebsites.net/setpeople',json=people)
    return sensorcreator()

@app.route('/',methods =['GET'])
def gotoinit():
    return sensorcreator()
#app.run(debug=True, port=8000) #run app in debug mode on port 5000
