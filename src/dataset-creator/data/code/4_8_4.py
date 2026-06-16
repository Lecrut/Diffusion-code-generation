import sys
def validate_input(user_choice: str) -> bool:
    allowed_options = ["A", "B"]
    return user_choice in allowed_options
class InputHandler:
    def __init__(self, primary_value: str):
        self.primary_value = primary_value
    def get_fallback(self) -> str:
        return "DEFAULT_OPTION"
    def process_input(self) -> tuple[str, bool]:
        is_valid = validate_input(self.primary_value)
        if not is_valid:
            fallback = self.get_fallback()
            print(f"Fallback activated. Using {fallback}")
            return fallback, False
        else:
            print(f"Primary input accepted: {self.primary_value}")
            return self.primary_value, True
if __name__ == '__main__':
    handler = InputHandler(primary_value="X")
    result, success = handler.process_input()