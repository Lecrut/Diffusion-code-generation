from .connect import GeminiConnection

class GeminiTester:
    def __init__(
        self,
        connection: GeminiConnection | None = None,
        model: str | None = None,
        temperature: float = 0.2,
    ) -> None:
        self.connection = connection or GeminiConnection(model=model)
        self.temperature = temperature

    def test_code(self, user_instruction: str, plan: str, code: str) -> str:
        system_prompt = (
            "You are Module 4 in a multi-agent diffusion coding pipeline. "
            "Evaluate the generated code based on the user's instruction and the provided plan. "
            "Return a concise feedback indicating whether the code meets the requirements or what issues it has."
            "Check if the code correctly implements the steps outlined in the plan and fulfills the user's instruction."
        )

        response = self.connection.generate(
            prompt=f"System: {system_prompt}\\n\\nUser Instruction: {user_instruction}\\n\\nPlan: {plan}\\n\\nGenerated Code:\\n{code}",
            temperature=self.temperature,
        )

        text = getattr(response, "text", None)
        if text:
            return text.strip() 
        return "Brak odpowiedzi tekstowej od modelu Gemini."