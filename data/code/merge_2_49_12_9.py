import re
class NumberValidator:
    def __init__(self):
        self.pattern = r'^\d+(\.\d+)?$'
    def sanitize_input(self, raw_value):
        if isinstance(raw_value, str):
            return raw_value.strip()
        elif not isinstance(raw_value, (int, float)):
            raise TypeError("Input must be a string or numeric type.")
        else:
            try:
                return str(float(raw_value)).strip('.')
            except ValueError:
                pass
    def is_valid_positive(self, value):
        sanitized = self.sanitize_input(value)
        if not isinstance(sanitized, str):
            raise TypeError("Sanitization failed or input type mismatch.")
        match = re.match(self.pattern, sanitized.strip())
        if not match:
            return False
        try:
            num_value = float(match.group(0))
            if num_value <= 0:
                return False
            formatted_num = f"{num_value:.15g}"
            if sanitized.strip() != formatted_num:
                raise ValueError("String and numeric representations do not match.")
        except (ValueError, OverflowError):
            return False
        return True
if __name__ == '__main__':
    validator = NumberValidator()
    test_cases = [
        "123",
        "-50.5",
        "+789",
        "  42  ",
        "",
        None,
        100,
        -10,
        "abc",
        ".5",
        "5.",
    ]
    for test_input in test_cases:
        try:
            result = validator.is_valid_positive(test_input)
            print(f"Input: {repr(test_input)} -> Valid Positive Number: {result}")
        except Exception as e:
            print(f"Input: {repr(test_input)} -> Error: {type(e).__name__}: {e}")