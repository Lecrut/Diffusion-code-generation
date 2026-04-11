import os

from dotenv import load_dotenv
from google import genai


class GeminiConnection:
    def __init__(self, model: str | None = None) -> None:
        load_dotenv()
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("Missing GEMINI_API_KEY in environment variables.")
        self.model = model or os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
        self.client = genai.Client(api_key=api_key)

    def generate(self, prompt: str, temperature: float = 0.2):
        return self.client.models.generate_content(
            model=self.model,
            contents=prompt,
            config={"temperature": temperature},
        )
