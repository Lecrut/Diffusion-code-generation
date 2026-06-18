import json
from datetime import datetime
class BooleanValidator:
    def __init__(self):
        self.log_entries = []
    def log(self, message, level="INFO"):
        timestamp = datetime.now().isoformat()
        entry = f"[{timestamp}] [{level}] {message}"
        self.log_entries.append(entry)
        print(entry)
    def validate_true(self, value):
        if isinstance(value, bool) and value is True:
            return {"valid": True, "reason": "Value is a boolean true"}
        elif isinstance(value, int) and value == 1 or str(value).lower() in ("yes", "y"):
            self.log(f"Warning: Value {value} coerced to True. Type was not bool.", level="WARNING")
            return {"valid": False, "reason": f"Incorrect type for strict validation (got {type(value).__name__})"}
        else:
            self.log(f"Invalid input: Expected boolean or 1/true equivalents", level="ERROR")
            return {"valid": False, "reason": "Value is not strictly True"}
    def validate_false(self, value):
        if isinstance(value, bool) and value is False:
            return {"valid": True, "reason": "Value is a boolean false"}
        elif isinstance(value, int) and value == 0 or str(value).lower() in ("no", "n"):
            self.log(f"Warning: Value {value} coerced to False. Type was not bool.", level="WARNING")
            return {"valid": False, "reason": f"Incorrect type for strict validation (got {type(value).__name__})"}
        else:
            self.log(f"Invalid input: Expected boolean or 0/false equivalents", level="ERROR")
            return {"valid": False, "reason": "Value is not strictly False"}
def run_validation():
    validator = BooleanValidator()
    sample_values = [True, False, True, False]
    for val in sample_values:
        result_true = validator.validate_true(val) if isinstance(val, (bool, int)) else None
        result_false = validator.validate_false(val) if isinstance(val, (bool, int)) else None
        test_cases = [1, 0, "yes", "no", "", None]
    print("\n--- Final Log Summary ---")
    for entry in validator.log_entries:
        print(entry)
if __name__ == '__main__':
    run_validation()