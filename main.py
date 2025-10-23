from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str

items = []

@app.get("/")
def get_items():
    return {"items": items}

@app.post("/")
def add_item(item: Item):
    items.append(item.name)
    return {"message": f"Added {item.name}"}
