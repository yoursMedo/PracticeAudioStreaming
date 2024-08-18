#  Setting up a simple Get Request 
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import os

app = FastAPI()


#  Setting up a server funcition 
#  This returns the audio as binary
def audio_streamer(file_path: str):
    with open(file_path, "rb") as audio_file:
        chunk_size = 1024 * 1024
        while True:
            chunk = audio_file.read(chunk_size)
            if not chunk:
                break
            yield chunk



@app.get("/")
async def main():
    return {
    "Hello", 
    "World",
    "We are developing",
    "Audio Streaming"
    }

@app.get("/music")
async def main(id: int = 1):
    if id == 1:
        file_path = os.path.join("Music", "Song.mp3")
        return StreamingResponse(audio_streamer(file_path), media_type="audio/mpeg")
    return None

