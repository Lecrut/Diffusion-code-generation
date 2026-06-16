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
            self.log(f"Validation Failed: Input '{value}' is not a boolean type.")
            return False
        valid_values = [True, False]
        if value in valid_values:
            status_msg = "Valid Boolean Value Detected."
            if value == True:
                self.log(status_msg + f"Value is TRUE")
            else:
                self.log(status_msg + f"Value is FALSE")
            return True
        self.log(f"Validation Failed: Input '{value}' does not match expected boolean values.")
        return False
if __name__ == '__main__':
    validator = BooleanValidator()
    test_cases = [True, False, 1, "yes", None, [], {}, object()]
    for case in test_cases:
        result = validator.validate_boolean(case)