from src.llm.planer import GeminiPlanner


if __name__ == "__main__":
    planner = GeminiPlanner()
    demo_prompt = "Napisz prosty API serwis do zarządzania zadaniami."
    print(planner.generate_plan(demo_prompt))
