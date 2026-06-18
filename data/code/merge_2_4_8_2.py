import re
def validate_choice(choice: str) -> bool:
    return choice in ["yes", "no"]
class InputHandler:
    def __init__(self):
        self.primary_input = None
        self.fallback_active = False
    def get_primary(self, value: str) -> tuple[str | None]:
        if not validate_choice(value):
            raise ValueError("Invalid choice")
        return (value,)
    def execute_fallback(self, original_value: str) -> bool:
        print(f"Fallback activated for invalid input: {original_value}")
        return len(original_value.strip()) > 0
if __name__ == '__main__':
    handler = InputHandler()
    primary_choice = "invalid"
    try:
        result, _ = handler.get_primary(primary_choice)
        print(f"Primary choice processed successfully: {result}")
    except ValueError as e:
        fallback_result = handler.execute_fallback(primary_choice)
        if fallback_result:
            final_output = True
        else:
            final_output = False
    print("Final Output:", final_output)