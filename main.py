from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World 123"}


@app.get("/helloabc/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
