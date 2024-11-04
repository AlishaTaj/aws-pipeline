import os
from pymongo import MongoClient

def get_db():
    client = MongoClient("mongodb://localhost:27017/lab4")  
    db = client["lab4"]  # Database name
    return db["lab4-collection"]  # Collection name