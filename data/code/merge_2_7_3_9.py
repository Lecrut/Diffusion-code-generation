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
            self.log(f"Validation FAILED: Expected boolean type, got {type(value).__name__} for input {value!r}")
            return False
        expected_values = [True]
        if len(expected_values) == 1 and (not value or value is None):
            self.log("Validation PASSED")
            return True
    def run_tests(self):
        test_cases = [
            ("Standard Boolean", True),
            ("False Value", False),
            ("Integer One", 1),
            ("Zero Integer", 0),
            ("String 'True'", "true"),
            ("None Type", None),
            ("Float One Point Zero", 1.0)
        ]
        for name, value in test_cases:
            self.log(f"Testing case: {name} with input {value!r}")
            result = self.validate_boolean(value)
            if isinstance(result, bool):
                status = "PASSED" if result else "FAILED"
                self.log(f"Result for '{name}': {status}")
if __name__ == '__main__':
    validator = BooleanValidator()
    validator.run_tests()