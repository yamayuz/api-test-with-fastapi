from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
async def hello():
    return {"message": "Hello World"}


@app.get("/prefectures/{prefecture_name}")
async def prefectures(prefecture_name: str):
    return {"prefecture_name": prefecture_name}


@app.get("/items/")
async def item(item_name: str = 'table', item_id: int = 1):
    return {
        "item_name": item_name,
        "item_id": item_id    
    }


# @app.get("/countries/{country_name}")
# async def country(country_name: str = 'japan', city_name:str = 'tokyo'):
#     return {
#         "country_name": country_name,
#         "city_name": city_name
#     }


@app.get("/countries/")
async def country(country_name: Optional[str] = None, 
                  country_no: Optional[int] = None):
    return {
        "country_name": country_name,
        "country_no": country_no
    }