from flask import Flask, jsonify, request
import json
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False },
    { "label": "Tercer elemento", "done": True },
    { "label": "Cuanto elemento", "done": False, "adress": "calle falsa 123" }
]


@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data # data cuerpo de la peticion
    decoded_object= json.loads(request_body)
    todos.append(decoded_object)
    return jsonify(todos)


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    print("ESTE ES EL ELEMENTO BORRADO: ",position)
    return jsonify(todos)




#al final siempre
if __name__ =='__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)