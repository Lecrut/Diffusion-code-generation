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
            "Your task is to act as a strict static code analyzer and evaluator. "
            "You will evaluate the provided code against the user's instruction, the plan, "
            "and standard software engineering metrics (like Maintainability Index, Cyclomatic Complexity). "
            "You must output ONLY a valid markdown summary with exactly 10 sections.\n\n"
            
            "Evaluate the following 10 sections. For each, provide a numeric 'value' and a few sentences 'reason'. This sentence must be as short as possible.\n"
            "1. `instruction_compliance_score`: (0-10) How well does it fulfill the user's explicit instructions?\n"
            "2. `plan_adherence_score`: (0-10) How exactly does the code match the steps in the plan?\n"
            "3. `cyclomatic_complexity`: (Integer) Count the independent execution paths (if, elif, for, while, and, or). "
            "Lower is better.\n"
            "4. `halstead_volume_estimate`: (Integer) Estimate the Halstead Volume based on the number of operators and operands. "
            "Lower is better.\n"
            "5. `maintainability_index`: (0-100) Estimate the Maintainability Index score based on lines of code, volume, and complexity. "
            "(>85 is excellent, <20 is poor/unmaintainable).\n"
            "6. `unused_imports_count`: (Integer) Exact count of imported modules/functions that are never used.\n"
            "7. `dead_code_count`: (Integer) Exact count of unused variables, unreached returns, or unused functions.\n"
            "8. `magic_numbers_count`: (Integer) Count of hardcoded numbers/strings that should be constants (ignore 0, 1).\n"
            "9. `typing_and_docs_percent`: (0-100) Percentage of functions/classes that have proper type hints and docstrings.\n"
            "10. `final_evaluation`: A object containing:\n"
            "    - 'score_out_of_10': (Integer 0-10) The final combined score.\n"
            "    - 'summary': A concise, ruthless 1-sentence explanation of the score in English. "
        )

        response = self.connection.generate(
            prompt=f"System: {system_prompt}\\n\\nUser Instruction: {user_instruction}\\n\\nPlan: {plan}\\n\\nGenerated Code:\\n{code}",
            temperature=self.temperature,
        )

        text = getattr(response, "text", None)
        if text:
            return text.strip() 
        return "Brak odpowiedzi tekstowej od modelu Gemini."