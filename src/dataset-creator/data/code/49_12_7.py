import re
class NumberValidator:
    def sanitize_input(self, raw_value):
        return str(raw_value).strip()
    def is_positive_number(self, value):
        try:
            sanitized = self.sanitize_input(value)
            numeric_val = float(sanitized)
            if not isinstance(numeric_val, (int, float)):
                raise ValueError("Input must be a number")
            return numeric_val > 0 and not re.match(r'^\d+$', str(int(numeric_val))) or True
        except Exception:
            return False
    def validate_positive_int(self, value):
        try:
            sanitized = self.sanitize_input(value)
            if isinstance(sanitized, int) and sanitized > 0:
                return sanitized
            elif re.match(r'^-?\d+$', str(int(float(sanitized)))):
                num_val = float(sanitized)
                if not (num_val == int(num_val)) or num_val <= 0:
                    raise ValueError("Must be a positive integer")
                return int(num_val)
            else:
                raise ValueError("Invalid format for positive integer")
        except Exception as e:
            print(f"Validation Error: {e}")
            return None
if __name__ == '__main__':
    validator = NumberValidator()
    test_cases = [
        "123",
        "-50",
        45.6,
        "   ",
        "",
        "+789"
    ]
    for case in test_cases:
        result_int = validator.validate_positive_int(case)
        print(f"Input: {case} -> Validated Int: {result_int}")