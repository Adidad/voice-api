from fastapi import FastAPI, Header, HTTPException
import base64

app = FastAPI()

API_KEY = "hcl_guvi"

@app.post("/api/voice-detection")
def voice_detection(
    payload: dict,
    x_api_key: str = Header(None)
):
    # 1. Check API key
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid API key"
        )

    # 2. Extract fields
    language = payload.get("language")
    audio_format = payload.get("audioFormat")
    audio_base64 = payload.get("audioBase64")

    if not language or not audio_format or not audio_base64:
        raise HTTPException(
            status_code=400,
            detail="Missing required fields"
        )

    if audio_format.lower() != "mp3":
        raise HTTPException(
            status_code=400,
            detail="Only MP3 format supported"
        )

    # 3. Decode Base64 (no processing yet)
    try:
        audio_bytes = base64.b64decode(audio_base64)
        with open("temp.mp3", "wb") as f:
            f.write(audio_bytes)
    except:
        raise HTTPException(
            status_code=400,
            detail="Invalid Base64 audio"
        )

    # 4. Dummy response
    return {
        "status": "success",
        "language": language,
        "classification": "HUMAN",
        "confidenceScore": 0.50,
        "explanation": "Dummy response – model not active"
    }
