import pymongo

from pymongo import MongoClient

# connect to the DATABASES
connection = MongoClient('localhost', 27017)

db = connection.test

# handlee to names connection
names = db.names

item = names.find_one()

print item['name']
