import os, copy
from flask import Flask, jsonify, request


app = Flask(__name__)


one = {
  "id": 5,
  "name": "Gabe",
  "lastname": "Focker",
  "age": 60,
  "gender": "Male",
  "parents": [0],
  "spouse": 14,
  "children": [12]
}
  

two = {
  "id": 55,
  "name": "Sarah",
  "lastname": "Doe",
  "age": 28,
  "gender": "Female",
  "parents": [0],
  "spouse": 5,
  "children": [12]
}


three = {
  "id": 34,
  "name": "Joe",
  "lastname": "Mama",
  "age": 30,
  "gender": "Male",
  "parents": [0],
  "spouse": 445,
  "children": [32]
}

four = {
  "id": 445,
  "name": "Chante",
  "lastname": "Sucker",
  "age": 38,
  "gender": "",
  "parents": [0],
  "spouse": 34,
  "children": [32]
}

five = {
  "id": 12,
  "name": "Dick",
  "lastname": "Focker",
  "age": 22,
  "gender": "Male",
  "parents": [5, 14],
  "spouse": 32,
  "children": [99]
}

six = {
  "id": 32,
  "name": "Ryona",
  "lastname": "Sucker",
  "age": 25,
  "gender": "Female",
  "parents": [34, 445],
  "spouse": 12,
  "children": [99]
}

seven = {
  "id": 99,
  "name": "Richard",
  "lastname": "Focker",
  "age": 5,
  "gender": "Male",
  "parents": [12, 32],
  "spouse": [0],
  "children": [0]
}


family =  {
  "members": [one, two, three, four, five, six, seven]
	}
 
def getMainID(a):
  for i in family["members"]:
    if a == i["id"]:
      return i
      
def getRelatives(member, types):
  tempList= []
  for types_id in member[types]:
    tempList.append(getMainID(types_id))
  member[types] = tempList
  return member

@app.route('/', methods=['GET'])
def hello():
  
  return jsonify(family)

@app.route('/members', methods=['GET'])
def by_Age():
  
  bele = copy.deepcopy(family["members"])
  bele.sort(key=lambda x:x['age'], reverse=True)
  response2 = jsonify({"status code":200, "data":bele})
  return response2
  
@app.route('/member/<int:id>')
def get_member(id):
  
  if id > 0:
    bele = copy.deepcopy(getMainID(id))
    if bele is not None:
      bele = getRelatives(bele, "parents")
      bele = getRelatives(bele, "children")
      return jsonify({"status_code":200, "data":bele})
      
  response = jsonify({"error": 400, "message":"no member found"})
  response.status_code = 400
  return response

app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))