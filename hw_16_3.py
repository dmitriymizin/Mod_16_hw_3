from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
async def get_users():
    return users

@app.post('/user/{username}/{age}')
async def create_user(username: str = Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser'),
                      age: int = Path(ge=18, le=120, description='Enter age', example='48')) -> str:
    new_id = str(int(max(users)) + 1)
    users[new_id] = f'Имя: {username}, возраст: {age}'
    return f'User {new_id} is registered'

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example='5')],
                      username: str, age: int) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f'The user {user_id} has been updated'

@app.delete('/user/{user_id}')
async def delete_user(user_id: str) -> str:
    users.pop(user_id)
    return f"User {user_id} has been deleted"

