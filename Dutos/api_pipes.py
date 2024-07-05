from fastapi import FastAPI, HTTPException
import json

app = FastAPI()

# Caminho para o arquivo db.json
DB_JSON_PATH = "C:/Users/nitro/OneDrive/Documentos/API - CILAMCE/Dutos/db.json"

@app.get("/data")
async def read_data():
    """Lê dados de db.json e retorna."""
    try:
        with open(DB_JSON_PATH, "r",  encoding="utf-8") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="db.json not found")
    