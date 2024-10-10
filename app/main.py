from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

file = './app/index.html'


@app.get("/")
async def root():
    return FileResponse(file, media_type='text/html')
