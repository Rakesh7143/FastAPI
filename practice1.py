from fastapi import FastAPI

app = FastAPI()

@app.post("/greet")
def greet_user(name: str):
    return {"message": f"Hello, {name}!"}

@app.get("/hello")
def say_hello():
    return {"message": "Hello, welcome to FastAPI!"}

# testing 1

# testing 2

# testing 3

