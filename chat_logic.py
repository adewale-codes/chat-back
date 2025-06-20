from transformers import pipeline
from config import MODEL_NAME

chat_pipeline = pipeline("text2text-generation", model="facebook/blenderbot_small-90M")

def get_bot_reply(message: str) -> str:
    result = chat_pipeline(message, max_new_tokens=50, pad_token_id=50256)
    return result[0]["generated_text"]
