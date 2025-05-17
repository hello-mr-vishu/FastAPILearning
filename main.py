from fastapi import FastAPI
import json

app = FastAPI()

def get_data():
    with open("patients.json", "r") as file:
        data = file.read()
    return data

@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/about")
def about():
    return {"message": "A fully functional API for managing patients."}

@app.get("/view")
def view():
    data = get_data()
    return data