import uvicorn
from fastapi import FastAPI


app = FastAPI()

@app.get("/hello_world")
def index():
    return { "message": "hello world"}

if __name__ == "__main__":
    uvicorn.run("hello:app", port=8000, reload=True)