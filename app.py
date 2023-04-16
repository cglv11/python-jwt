from fastapi import FastAPI
from dotenv import load_dotenv
from routes.auth import auth_routes
from routes.users_github import users_github

app = FastAPI(
    title="REST API with FastAPI and Auth JWT",
    description="This is a simple rest api with fastAPI",
    version="0.0.1",
)

app.include_router(auth_routes, prefix='/api')
app.include_router(users_github, prefix='/api')

load_dotenv()