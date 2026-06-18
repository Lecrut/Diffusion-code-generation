import re
class NumberValidator:
    def sanitize_input(self, raw_data):
        if not isinstance(raw_data, str):
            raise TypeError("Input must be a string.")
        cleaned = raw_data.strip()
        if not cleaned:
            return None
        match = re.match(r'^[\d\.]+$', cleaned)
        if not match:
            raise ValueError(f"Invalid numeric format: {raw_data}")
        try:
            float(cleaned)
            return cleaned
        except ValueError:
            raise ValueError("Input contains non-numeric characters.")
    def is_positive(self, value):
        num = self.sanitize_input(value)
        if not num or num == "0":
            return False
        try:
            float(num) > 0
            return True
        except (ValueError, TypeError):
            raise ValueError("Sanitized input failed numeric conversion.")
def validate_positive_number(raw_value):
    validator = NumberValidator()
    if not isinstance(raw_value, str):
        raw_str = str(raw_value)
        try:
            num = float(raw_str.strip())
            if num <= 0:
                raise ValueError("Number must be positive.")
            return True
        except (ValueError, TypeError):
            pass
    sanitized = validator.sanitize_input(raw_value)
    if not sanitized or sanitized == "0":
        raise ValueError("Input is zero or empty after sanitization.")
    try:
        num = float(sanitized)
        if num <= 0:
            raise ValueError(f"Number must be positive. Received: {num}")
        return True
    except (ValueError, TypeError):
        raise ValueError("Invalid number format provided.")
if __name__ == '__main__':
    test_cases = [
        "123",
        "-50",
        456.789,
        "",
        "abc",
        ".5",
        "   ",
        "1e2"
    ]
    for case in test_cases:
        try:
            result = validate_positive_number(case)
            print(f"Input '{case}' -> Validated as positive")
        except ValueError as e:
            print(f"Input '{case}' -> Error: {e}")