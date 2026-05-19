from src.llm.planer import GeminiPlanner
from src.llm.tester import GeminiTester
from src.tokenizer import CodeTokenizer
from src.diffusion import DiffusionModel
from src.tools import executor


if __name__ == "__main__":
    planner = GeminiPlanner()
    user_prompt = input("Enter prompt: ")
    plan = planner.generate_plan(user_prompt)
    print("Generated Plan:")
    print(plan)

    tokenizer = CodeTokenizer()
    print("\nEncoded Plan:")
    print(tokenizer.encode(plan))
    print("\nDecoded Plan:")
    print(tokenizer.decode(tokenizer.encode(plan)))

    model = DiffusionModel()
    generated_code = None 
    num_attempts = 0

    while executor(generated_code) is False:
        generated_code = model.generate_code(plan)
        num_attempts += 1

        if num_attempts > 5:
            print("Failed to generate valid code after 5 attempts.")
            raise Exception("Code generation failed after 5 attempts.")
    
    print("\nGenerated Code:")
    print(generated_code)

    print('#' * 50)

    tester = GeminiTester()
    feedback = tester.test_code(user_prompt, plan, generated_code)
    print("\nFeedback:")
    print(feedback)

    