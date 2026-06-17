import re
class NumberValidator:
    def __init__(self):
        self.pattern = r'^\d+(\.\d+)?$'
    def sanitize_input(self, text):
        return str(text).strip() if isinstance(text, (str, int)) else None
    def is_positive_number(self, value):
        try:
            cleaned_value = self.sanitize_input(value)
            if not cleaned_value or not re.match(self.pattern, cleaned_value):
                raise ValueError("Input must be a valid positive number.")
            num = float(cleaned_value)
            return num > 0 and not math.isnan(num)
        except (ValueError, TypeError, OverflowError):
            return False
import math
if __name__ == '__main__':
    validator = NumberValidator()
    test_cases = [
        "123",
        "+45.67",
        "-89",
        0,
        None,
        "",
        "abc",
        "\t\t"
    ]
    for case in test_cases:
        result = validator.is_positive_number(case)
        print(f"Input: {case!r} -> Valid Positive Number: {result}")