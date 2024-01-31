from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World!!"}

if __name__ == '__main__':
    app.run(debug=True)