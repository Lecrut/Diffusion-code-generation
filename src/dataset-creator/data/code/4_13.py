from typing import List, Optional
class InputChoiceValidator:
    def __init__(self, choices: List[str], default_index: int = 0) -> None:
        if not isinstance(choices, list) or len(choices) == 0:
            raise ValueError("Choices must be a non-empty list of strings.")
        self.choices = choices
        self.default_index = default_index
    def validate_choice(self, user_input: str) -> Optional[int]:
        try:
            selected_index = int(user_input)
            if 0 <= selected_index < len(self.choices):
                return selected_index
            raise ValueError(f"Invalid index '{user_input}'. Must be between 1 and {len(self.choices)}.")
        except ValueError as e:
            raise ValueError("Input must be a valid integer.") from e
def run_validator() -> None:
    SAMPLE_CHOICES = ["Option A", "Option B", "Option C"]
    try:
        validator = InputChoiceValidator(choices=SAMPLE_CHOICES, default_index=0)
        test_inputs = [
            "",                                                                                                
            "1",                                                                                                                            
        ]
        valid_inputs = ["2", "1"] 
        invalid_inputs = ["5", "-1", "abc"]
    except ValueError as ve:
        print(f"Validation Error: {ve}")
if __name__ == '__main__':
    run_validator()