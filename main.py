from fastapi import FastAPI

app = FastAPI()

@app.get("/greet/{username}")
async def read_user(username: str):
    return {"message": f"Hello {username}"}
