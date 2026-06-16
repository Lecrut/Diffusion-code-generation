from typing import List, Optional
class InputChoiceValidator:
    def __init__(self, choices: List[str], default_index: int = 0) -> None:
        self.choices: List[str] = [choice.strip() for choice in choices if choice.strip()]
        self.default_index: int = max(0, min(default_index, len(self.choices) - 1))
    def validate_input(self, user_choice: str) -> Optional[int]:
        normalized_choice = user_choice.strip().lower()
        try:
            index = self.choices.index(normalized_choice)
            return index
        except ValueError:
            raise ValueError(f"Invalid option '{user_choice}'. Available options are: {', '.join(self.choices)}")
def get_validated_target(validator: InputChoiceValidator, user_input: str) -> int:
    try:
        return validator.validate_input(user_input)
    except ValueError as e:
        raise e
if __name__ == '__main__':
    VALIDATION_OPTIONS = ["apple", "banana", "cherry"]
    try:
        validator = InputChoiceValidator(VALIDATION_OPTIONS)
        simulated_inputs = [
            "Apple",                                                                                                      
            "banana"
        ]
        for inp in simulated_inputs:
            target_index = get_validated_target(validator, inp)
            print(f"Selected Target Index: {target_index} -> Choice: {VALIDATION_OPTIONS[target_index]}")
    except ValueError as ve:
        print(f"\nError encountered during validation:")
        print(f"{ve}")