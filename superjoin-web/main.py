__author__ = 'Paolo'

from bottle import route, run, template, get, response, static_file
import pymongo
import MongoEncoder

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

@route('/main.htm')
def main():
    raise static_file('main.htm', root='')


@get('/slices')
def getslices():

    db = pymongo.Connection()['mr_demo']

    tables = list(db.slices.find({}))
    tableNames = [t['name'] for t in tables]

    return {
        'count' : len(tables),
        'slices' : tableNames
    }

@post
def join(data):
    sys.stdout.write("i am joining the data with slice 1: %d and slice 2: %d" % (data.slice1, data.slice2))

@route('/tabledata/<name>')
def gettabledata(name):
    db = pymongo.Connection()['mr_demo']
    data_collection = db[name]
    
    data = list(data_collection.find({}))
    json_data = dumps(data)

    return { data : json_data }

run(host='localhost', port=8080, reloader=True)