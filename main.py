from src.llm.planer import GeminiPlanner
from src.tokenizer import CodeTokenizer


if __name__ == "__main__":
    planner = GeminiPlanner()
    demo_prompt = "Napisz prosty API serwis do zarządzania zadaniami."
    plan = planner.generate_plan(demo_prompt)
    print("Generated Plan:")
    print(plan)

    tokenizer = CodeTokenizer()
    print("\nEncoded Plan:")
    print(tokenizer.encode(plan))
    print("\nDecoded Plan:")
    print(tokenizer.decode(tokenizer.encode(plan)))