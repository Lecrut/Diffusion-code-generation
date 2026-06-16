import sys
from datetime import datetime
class BooleanValidator:
    def __init__(self):
        self.log_level = "INFO"
    def log(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] [{self.log_level}] {message}")
    def validate_bool_value(self, value):
        if isinstance(value, bool) and (value is True or value is False):
            return {"valid": True, "reason": f"Value '{value}' is a valid boolean."}
        invalid_types = []
        for t in [int, float, str]:
            try:
                val = int(value) if isinstance(value, (str,)) else value
                bool(val)
                invalid_types.append(t.__name__)
            except ValueError:
                pass
        return {
            "valid": False, 
            "reason": f"Value '{value}' is not a boolean. Attempted conversions for types: {', '.join(invalid_types)} failed." if invalid_types else f"Value '{value}' cannot be converted to bool directly without ambiguity.",
            "input_type": type(value).__name__
        }
    def run_validation_suite(self):
        test_cases = [True, False, 1, -1, 0.5, "", None, [], {}, set()]
        self.log("Starting Boolean Validation Suite")
        for item in test_cases:
            result = self.validate_bool_value(item)
            self.log(f"Input: {item} (Type: {type(item).__name__}) -> Result: {'Valid' if result['valid'] else 'Invalid'} - Reason: {result['reason']}")
if __name__ == '__main__':
    validator = BooleanValidator()
    validator.run_validation_suite()