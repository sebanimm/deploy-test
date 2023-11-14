from typing import Optional
from beanie import Document
from pydantic import BaseModel, EmailStr
from models.events import Event


class User(Document):
    email: EmailStr
    password: str
    events: Optional[list[Event]]

    class Settings:
        name = "users"

    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
                "events": [],
            }
        }


class UserSignIn(BaseModel):
    email: EmailStr
    password: str
