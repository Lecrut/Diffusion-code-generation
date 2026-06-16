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
            self.log(f"Invalid type: expected bool, got {type(value).__name__}. Value rejected.")
            return False
        valid_values = [True, False]
        if value in valid_values:
            status_msg = "Valid boolean value."
            if value is True:
                status_msg += " Confirmed as TRUE."
            else:
                status_msg += " Confirmed as FALSE."
            self.log(status_msg)
            return True
        self.log(f"Invalid boolean literal provided. Value rejected.")
        return False
if __name__ == '__main__':
    validator = BooleanValidator()
    test_cases = [True, False, 1, "true", None, [], {}, object()]
    for case in test_cases:
        result = validator.validate_boolean(case)