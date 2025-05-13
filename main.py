from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# Allow CORS for React frontend (assuming it's running on http://localhost:3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://food-buddy-gules.vercel.app"],  # Only allow this origin
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)
# Dummy restaurant data
class Restaurant(BaseModel):
    id: int
    name: str
    image: str
    description: str

restaurants = [
    Restaurant(id=1, name="Spice Villa", image="https://via.placeholder.com/300x200?text=Spice+Villa", description="Authentic Indian cuisine with a modern twist."),
    Restaurant(id=2, name="Burger Hub", image="https://via.placeholder.com/300x200?text=Burger+Hub", description="Juicy burgers and crispy fries served fresh."),
    Restaurant(id=3, name="Green Delight", image="https://via.placeholder.com/300x200?text=Green+Delight", description="Vegan and vegetarian meals for a healthy lifestyle.")
]

# Endpoint to fetch restaurant data
@app.get("/restaurants")
def get_restaurants():
    return restaurants

if __name__ == "__main__":
    # This is for running directly with Python (not required with uvicorn)
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
