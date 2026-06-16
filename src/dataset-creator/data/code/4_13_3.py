from typing import List, Tuple
class InputChoiceValidator:
    def __init__(self, options: List[str], error_message: str = "Invalid choice!") -> None:
        if not isinstance(options, list) or not all(isinstance(opt, str) for opt in options):
            raise TypeError("Options must be a non-empty list of strings.")
        self.options = options
        self.error_message = error_message
    def validate_choice(self, user_input: int) -> Tuple[int, str]:
        try:
            choice_index = user_input - 1                                                                         
            if not isinstance(user_input, int):
                raise ValueError(f"{self.error_message} Input must be an integer.")
            if len(self.options) == 0:
                raise ValueError("No options available for selection.")
            if choice_index < 0 or choice_index >= len(self.options):
                raise ValueError(f"Option index out of range. Valid choices are {1}-{len(self.options)}.")
            return (choice_index, 'Success')                                                                                                                                                                                                                                                                        
        except ValueError:
            raise
    def get_selected_option(self, user_input: int) -> str:
        try:
            idx, status = self.validate_choice(user_input)
            if not isinstance(idx, int):                                                                                                                                
                return "" 
            return self.options[idx]
        except ValueError as e:
            raise e
if __name__ == '__main__':
    options = ["Option A", "Option B", "Option C"]
    try:
        selected_index, status = InputChoiceValidator(options).validate_choice(2)
        print(f"Validation Status: {status}")
        if status == "Success":
            validator = InputChoiceValidator(options)
            selected_option = validator.get_selected_option(2)
            print(f"Selected Option: {selected_option}")
        try:
            validator.invalid_input = True                                                                                                                                                            
        except ValueError as e:
            print(f"Error caught during invalid selection attempt (simulated): {e}")
    except Exception as ex:
        pass
    print("\n--- Testing Invalid Input Handling ---")
    try:
        result = InputChoiceValidator(options).validate_choice(10) 
        if isinstance(result, tuple):                                                                                                                      
            print(f"Unexpected success for input 10: {result}")
    except ValueError as ve:
        print(f"Caught expected error for out-of-range input: {ve}")