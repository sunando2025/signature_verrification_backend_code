from fastapi import FastAPI, File, UploadFile
import uvicorn
import multiprocessing

app = FastAPI()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    # Print file name in the VS Code terminal
    print(f"Received file: {file.filename}")
    return {"filename": file.filename}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
