from .connect import GeminiConnection


class GeminiPlanner:
    def __init__(
        self,
        connection: GeminiConnection | None = None,
        model: str | None = None,
        temperature: float = 0.2,
    ) -> None:
        self.connection = connection or GeminiConnection(model=model)
        self.temperature = temperature

    def generate_plan(self, user_prompt: str) -> str:
        system_prompt = (
            "You are Module 1 in a multi-agent diffusion coding pipeline. "
            "Transform the user's request into a sequential implementation plan in Polish. "
            "Return only the plan as numbered steps."
        )

        response = self.connection.generate(
            prompt=f"System: {system_prompt}\\n\\nUser: {user_prompt}",
            temperature=self.temperature,
        )

        text = getattr(response, "text", None)
        if text:
            return text.strip()
        return "Brak odpowiedzi tekstowej od modelu Gemini."
