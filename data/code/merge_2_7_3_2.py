import sys
from datetime import datetime
class BooleanValidator:
    def __init__(self):
        self.log_level = "INFO"
    def log(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] [{self.log_level}] {message}")
    def validate_boolean(self, value):
        if not isinstance(value, bool):
            return False, "Input is not a boolean type"
        valid_values = [True, False]
        if value not in valid_values:
            return False, f"Invalid boolean value. Expected {valid_values}, got {value}"
        self.log(f"Validated input: {value}")
        return True, "Validation successful"
def run_validation_tests():
    validator = BooleanValidator()
    test_cases = [
        (True, "Standard true"),
        (False, "Standard false"),
        ("true", "String representation of true"),
        ("false", "String representation of false"),
        (1, "Integer one"),
        (0, "Integer zero"),
        ([], "Empty list"),
        ({}, "Empty dict"),
    ]
    for test_input, description in test_cases:
        is_valid, message = validator.validate_boolean(test_input)
        if not is_valid:
            status_str = f"FAILED - {message}"
        else:
            status_str = "PASSED"
        print(f"\nTest Case: {description}")
        print(f"Input Value: {test_input!r} (Type: {type(test_input).__name__})")
        print(f"Result: {status_str}\n")
if __name__ == '__main__':
    run_validation_tests()