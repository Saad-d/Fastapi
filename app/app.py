from fastapi import FastAPI, HTTPException, File, UploadFile, Form, Depends
from app.schemas import postCreate
from app.db import Posts, create_db_table,get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_table()
    yield

app = FastAPI(lifespan=lifespan)
