from typing import List, Optional
class InputChoiceValidator:
    def __init__(self, choices: List[str], default_index: int = 0) -> None:
        self.choices = choices
        self.default_index = default_index
        if not isinstance(choices, list):
            raise TypeError("Choices must be a list.")
        if len(self.choices) == 0:
            raise ValueError("Cannot select from an empty list of choices.")
        try:
            int_val = int(default_index)
        except ValueError as e:
            raise TypeError(f"Default index must be convertible to integer. Got {default_index}.") from e
        if not (0 <= self.default_index < len(self.choices)):
            raise IndexError(f"Default index {self.default_index} is out of bounds for choices with length {len(self.choices)}.")
    def validate_and_select(
        self, 
        user_input: Optional[str] = None
    ) -> str:
        if user_input is None:
            return self.choices[self.default_index]
        try:
            selected_index = int(user_input)
            if 0 <= selected_index < len(self.choices):
                return self.choices[selected_index]
            else:
                raise ValueError(f"Index {selected_index} out of range. Valid indices are from 0 to {len(self.choices)-1}.")
        except ValueError as e:
            try:
                int(user_input)
            except ValueError:
                raise TypeError(f"Invalid input '{user_input}'. Please enter an integer.") from None
            raise IndexError(f"Index {selected_index} out of range. Valid indices are from 0 to {len(self.choices)-1}.")
if __name__ == '__main__':
    validator = InputChoiceValidator(
        choices=["Option A", "Option B", "Option C"], 
        default_index=2
    )
    test_cases: List[Optional[str]] = [None, "0", "1", "invalid_input", "5"]
    for i, input_val in enumerate(test_cases):
        try:
            result = validator.validate_and_select(input_val)
            print(f"Test Case {i+1} (Input: '{input_val}' or None): Selected -> {result}")
        except Exception as ex:
            print(f"Test Case {i+1}: Raised exception - {type(ex).__name__}: {ex}")