from typing import List, Optional
class InputChoiceValidator:
    def __init__(self, choices: List[str], default_index: int = 0) -> None:
        self.choices = choices
        self.default_index = default_index
        if not isinstance(choices, list):
            raise TypeError("Choices must be a list.")
        if len(self.choices) == 0:
            raise ValueError("Cannot select from an empty set of options.")
        if not (0 <= self.default_index < len(self.choices)):
            raise IndexError(f"Default index {self.default_index} is out of bounds for choices with length {len(choices)}.")
    def validate_choice(self, user_input: str) -> Optional[int]:
        if not isinstance(user_input, str) or user_input.strip() == "":
            raise ValueError("User input must be a non-empty string.")
        normalized_input = user_input.lower().strip()
        for index, choice in enumerate(self.choices):
            if choice.lower() == normalized_input:
                return index
        return self.default_index
    def get_selected_target(self, user_input: str = "") -> Optional[str]:
        try:
            index = self.validate_choice(user_input)
            if index is not None and 0 <= index < len(self.choices):
                return self.choices[index]
            else:
                raise ValueError(f"Invalid selection provided by user.")
        except (ValueError, IndexError) as e:
            if isinstance(e, ValueError):
                print(f"Validation Error: {e}")
            else:
                raise
if __name__ == '__main__':
    options = ["apple", "banana", "cherry"]
    validator = InputChoiceValidator(choices=options)
    test_inputs = [
        "",                                                                                                                                            
        "APPLE",                                        
        "BANANA",                   
        "GRAPE",                                                                                                       
        "invalid"               
    ]
    for i, inp in enumerate(test_inputs):
        print(f"\n--- Test Case {i+1}: Input = '{inp}' ---")
        try:
            result_str = validator.get_selected_target(inp)
            if result_str is None:
                print("Result:", result_str)
            else:
                print(f"Selected Target: {result_str}")
        except ValueError as ve:
            print(f"Caught Exception (ValueError): {ve}")