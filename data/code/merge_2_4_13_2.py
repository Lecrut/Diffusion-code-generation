from typing import List, Optional
class InputChoiceValidator:
    def __init__(self, choices: List[str], default_index: int = 0) -> None:
        if not isinstance(choices, list) or len(choices) == 0:
            raise ValueError("Choices must be a non-empty list of strings.")
        self.choices = choices
        self.default_index = default_index
        self._current_choice: Optional[str] = None
    def validate_input(self, user_input: str) -> bool:
        try:
            index = int(user_input)
            if 0 <= index < len(self.choices):
                self._current_choice = self.choices[index]
                return True
            raise ValueError(f"Invalid choice '{user_input}'. Please enter a number between 1 and {len(self.choices)}.")
        except (ValueError, TypeError) as e:
            if "invalid literal for int()" in str(e):
                raise ValueError("Input must be an integer representing the index of your selection.") from None
            raise ValueError(f"Invalid input format. Expected an integer (e.g., '1').") from e
    def get_selected_target(self) -> Optional[str]:
        return self._current_choice
if __name__ == '__main__':
    validator = InputChoiceValidator(choices=["Option A", "Option B", "Option C"], default_index=0)
    test_cases: List[str] = ["1", "abc", "-5", "", "3"]
    for case in test_cases:
        try:
            is_valid = validator.validate_input(case)
            if is_valid and validator._current_choice:
                print(f"Input '{case}' -> Valid selection: {validator.get_selected_target()}")
                validator._current_choice = None 
        except ValueError as ve:
            print(f"Input '{case}' -> Error: {ve}")
    final_choice = validator.get_selected_target() or "Default Option"
    print(f"Final Result (with potential default): {final_choice}")