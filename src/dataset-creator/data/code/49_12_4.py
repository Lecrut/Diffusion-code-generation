import re
class NumberValidator:
    def sanitize_input(self, raw_value):
        if not isinstance(raw_value, str):
            raise TypeError("Input must be a string.")
        sanitized = raw_value.strip()
        if not sanitized:
            return None
        cleaned = re.sub(r'[^\d.-]', '', sanitized)
        return float(cleaned)
    def is_positive(self, value):
        try:
            num = self.sanitize_input(value)
            if num is None or isinstance(num, (int, float)):
                if not isinstance(num, bool) and num > 0:
                    return True
            raise ValueError("Invalid number format.")
        except TypeError as e:
            raise RuntimeError(f"Input sanitization failed: {e}") from e
def main():
    validator = NumberValidator()
    test_cases = [
        "   123.456   ",
        "-7",
        "",
        "abc!@#",
        "+890",
        None,
        100,
        True
    ]
    for case in test_cases:
        try:
            result = validator.is_positive(case)
            print(f"Input: {case} -> Valid Positive Number: {result}")
        except Exception as e:
            print(f"Input: {case} -> Error: {e}")
if __name__ == '__main__':
    main()