from fastapi import FastAPI
import asyncio
import datetime

app = FastAPI()

@app.get("/")
async def read_root():
    """
    Root endpoint for the FastAPI application.
    Returns a simple welcome message.
    """
    return {"message": "Hello, FastAPI!"}


@app.get("/get-report/{report_id}")
async def get_report(report_id: int):
    """
    Endpoint to retrieve an item by its ID.
    """

    # simulate a slow response
    api_hit_time = datetime.datetime.now()
    await asyncio.sleep(30)
    return {"report_id": report_id, "entry_time": str(api_hit_time), "exit_time": str(datetime.datetime.now())}
