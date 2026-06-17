import re
class NumberValidator:
    def __init__(self):
        self.pattern = r'^[\d]+(\.[\d]+)?$'
    def sanitize_input(self, raw_data):
        if not isinstance(raw_data, str):
            raise TypeError("Input must be a string.")
        return raw_data.strip()
    def validate_positive_number(self, input_str):
        try:
            sanitized = self.sanitize_input(input_str)
            numeric_value = float(sanitized)
            if numeric_value <= 0 or not re.match(r'^[\d]+(\.[\d]+)?$', sanitized.replace('.', '')):
                raise ValueError("Input must be a positive number.")
            return True, numeric_value
        except (ValueError, TypeError):
            return False, None
if __name__ == '__main__':
    validator = NumberValidator()
    test_cases = [
        "10",
        "-5.2",
        "",
        "  abc  ",
        "+3.14"
    ]
    for case in test_cases:
        is_valid, value = validator.validate_positive_number(case)
        if is_valid:
            print(f"{case!r} -> Valid ({value})")
        else:
            print(f"{case!r} -> Invalid")