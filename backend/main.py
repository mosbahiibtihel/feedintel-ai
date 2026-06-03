from fastapi import FastAPI
from backend.supabase_client import supabase

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FeedIntel AI is running"}

@app.get("/products")
def get_products():
    response = supabase.table("products").select("*").execute()
    return response.data 