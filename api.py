import pymysql
from flask import Flask, jsonify, request

host = ${host}
user = ${user}
password = ${password}
database = 'bus'
port = 3306


#connection = pymysql.connect(host = host, port = port, user = user, password = password, database = database)
#cursor = connection.cursor()


app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add():
    try:
        _json = request.json
        _busno = _json['busno']
        _startpoint = _json['startpoint']
        _endpoint = _json['endpoint']
        connection = pymysql.connect(host = host, port = port, user = user, password = password, database = database)
        cursor = connection.cursor()
        sqlQuery = "INSERT INTO details(bus_no, start_point, end_point) VALUES(%s, %s, %s)"
        bindData = (_busno, _startpoint, _endpoint)
        cursor.execute(sqlQuery, bindData)
        connection.commit()
        response = jsonify({'response':'bus details added successfully!'})
        response.status_code = 200
        cursor.close()
        connection.close()
        return response
    except Exception as e:
        return str(e), 500

@app.route('/update', methods=['PUT'])
def update():
    try:
        _json = request.json
        _busno = _json['busno']
        _start = _json['startpoint']
        _end = _json['endpoint']
        connection = pymysql.connect(host = host, port = port, user = user, password = password, database = database)
        cursor = connection.cursor()
        sqlQuery = "update details set start_point=%s, end_point=%s where bus_no=%s"
        bindData = (_start, _end, _busno)
        cursor.execute(sqlQuery, bindData)
        connection.commit()
        response = jsonify({'response':'bus details updated successfully!'})
        cursor.close()
        connection.close()
        return response
    except Exception as e:
        return str(e), 500

@app.route('/get', methods=['GET'])
def get():
    try:
        _json = request.json
        _busno = _json['busno']
        connection = pymysql.connect(host = host, port = port, user = user, password = password, database = database)
        cursor = connection.cursor()
        sqlQuery = "select * from details where bus_no=%s"
        bindData = (_busno, )
        cursor.execute(sqlQuery, bindData)
        connection.commit()
        ret = cursor.fetchall()
        response = jsonify({'busno' : ret[0][0], 'startpoint' : ret[0][1], 'endpoint' : ret[0][2]})
        cursor.close()
        connection.close()
        return response
    except Exception as e:
        return str(e), 500

@app.route('/delete', methods=['DELETE'])
def delete():
    try:
        _json = request.json
        _busno = _json['busno']
        connection = pymysql.connect(host = host, port = port, user = user, password = password, database = database)
        cursor = connection.cursor()
        sqlQuery = "delete from details where bus_no=%s"
        bindData = (_busno)
        cursor.execute(sqlQuery, bindData)
        connection.commit()
        response = jsonify({'response' : 'bus detail deleted successfully'})
        cursor.close()
        connection.close()
        return response
    except Exception as e:
        return str(e), 500

@app.route('/')
def home():
    return "It's working"

if __name__=="__main__":
    app.run(debug=True,port=8000)
