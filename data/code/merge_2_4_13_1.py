from typing import List, Optional
class InputChoiceValidator:
    def __init__(self, choices: List[str], default_index: int = 0) -> None:
        self.choices: List[str] = list(choices)
        if not (default_index >= 0 and default_index < len(self.choices)):
            raise ValueError(f"Default index {default_index} must be between 0 and {len(self.choices)-1}")
    def validate_choice(self, user_input: str) -> Optional[int]:
        try:
            return self.choices.index(user_input)
        except ValueError as e:
            raise ValueError(f"Invalid selection '{user_input}'. Available options are {self.choices}") from e
if __name__ == '__main__':
    VALIDATION = InputChoiceValidator(choices=["apple", "banana", "cherry"], default_index=1)
    SAMPLE_INPUTS = ["apple", 99, "", None]
    for item in SAMPLE_INPUTS:
        try:
            result = VALIDATION.validate_choice(str(item)) if isinstance(item, (int, float)) else VALIDATION.validate_choice(item)
            print(f"Input {item} -> Index {result}")
        except ValueError as ve:
            print(f"Error for input {item}: {ve}")
    try:
        INVALID_INPUT = "date"
        result = VALIDATION.validate_choice(INVALID_INPUT)
    except ValueError as e:
        print(f"Catch error for '{INVALID_INPUT}': {e}")