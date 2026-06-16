import json
from datetime import datetime
class BooleanValidator:
    def __init__(self):
        self.log_level = "INFO"
    def log(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] [{self.log_level}] {message}")
    def validate_boolean(self, value):
        if isinstance(value, bool) and (value is True or value is False):
            return {"valid": True, "reason": "Standard boolean type"}
        try:
            int_value = int(str(value).lower())
            if int_value == 1:
                return {"valid": True, "reason": "String representation of 'True'"}
            elif int_value == 0:
                return {"valid": True, "reason": "String representation of 'False' or empty string treated as False"}
        except ValueError:
            pass
        if isinstance(value, (int, float)):
            try:
                bool_result = bool(int(float(value)))
                self.log(f"Numeric value {value} converted to boolean {bool_result}")
                return {"valid": True, "reason": f"Numeric conversion resulted in {bool_result}"}
            except Exception as e:
                pass
        if isinstance(value, str):
            lower_val = value.lower().strip()
            if lower_val == 'true' or lower_val == '1':
                return {"valid": True, "reason": f"String '{value}' interpreted as True"}
            elif lower_val in ('false', '', '0'):
                return {"valid": True, "reason": f"String '{value}' interpreted as False"}
        self.log(f"Invalid input type: {type(value).__name__}, value: {value}")
        return {"valid": False, "reason": f"Unsupported type or invalid format for boolean validation"}
if __name__ == '__main__':
    validator = BooleanValidator()
    test_cases = [
        True,
        False,
        1,
        -1,
        0.5,
        "",
        "true",
        "TRUE",
        "false",
        "FALSE",
        "yes",
        "no",
        None,
        [],
        {},
    ]
    for test_val in test_cases:
        result = validator.validate_boolean(test_val)
        print(f"Input: {test_val} -> Result: {result}")