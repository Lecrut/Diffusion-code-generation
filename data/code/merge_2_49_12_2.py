import re
class NumberValidator:
    def sanitize_input(self, user_input):
        if not isinstance(user_input, str):
            raise TypeError("Input must be a string.")
        sanitized = re.sub(r'[^0-9.-]', '', user_input.strip())
        return sanitized
    def is_positive_number(self, value):
        try:
            num = float(value)
            if not isinstance(num, (int, float)):
                raise ValueError("Converted value must be numeric.")
            if num <= 0:
                raise ValueError(f"Value {num} is not positive. Must be greater than zero.")
            return True
        except ValueError as e:
            print(f"Validation Error: {e}")
            return False
def run_validation():
    validator = NumberValidator()
    sample_inputs = [
        "123",
        "-50",
        "",
        "   45.67   ",
        "+89",
        "abc"
    ]
    for test_input in sample_inputs:
        print(f"\nTesting input: '{test_input}'")
        try:
            cleaned = validator.sanitize_input(test_input)
            if not cleaned:
                print("Result: Empty string after sanitization.")
                continue
            is_valid = validator.is_positive_number(cleaned)
            print(f"Sanitized value: {cleaned}")
            print(f"is_positive check result: {'Valid' if is_valid else 'Invalid'}")
        except Exception as e:
            print(f"Exception occurred during validation of '{test_input}': {e}")
if __name__ == '__main__':
    run_validation()