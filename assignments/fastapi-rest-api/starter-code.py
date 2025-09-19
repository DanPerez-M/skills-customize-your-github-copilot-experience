from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: str = ""

items: List[Item] = []

@app.get("/items", response_model=List[Item])
def get_items():
    return items

@app.post("/items", response_model=Item)
def add_item(item: Item):
    items.append(item)
    return item

# Extensión sugerida para la tarea:
# @app.put("/items/{item_id}")
# @app.delete("/items/{item_id}")
