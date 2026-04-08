from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"Mon premier message": "Hello World"}