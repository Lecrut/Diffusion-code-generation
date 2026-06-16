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
            self.log(f"Validation Failed: Expected boolean type, got {type(value).__name__} for input {value!r}")
            return False
        valid_values = [True, False]
        if value in valid_values:
            status_msg = "Valid Boolean Value Detected" if value else "Invalid Boolean Value Detected (False)"
            self.log(f"{status_msg}: Input is {value!r}")
            return True
        else:
            self.log(f"Validation Failed: Unexpected boolean value {value!r} encountered")
            return False
if __name__ == '__main__':
    validator = BooleanValidator()
    test_cases = [True, False, 1, "true", None, [], {}, object()]
    for case in test_cases:
        result = validator.validate_boolean(case)