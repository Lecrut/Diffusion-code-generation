import re
class PositiveNumberValidator:
    def sanitize_input(self, raw_data):
        if not isinstance(raw_data, str):
            raise TypeError("Input must be a string.")
        cleaned = ''.join(filter(str.isdigit, raw_data))
        return int(cleaned) if cleaned else None
    def validate_positive_number(self, input_value):
        try:
            number = self.sanitize_input(input_value)
            if number is None or not isinstance(number, (int, float)):
                raise ValueError("Sanitized data must be a valid numeric type.")
            if number <= 0:
                return False
            return True
        except Exception as e:
            return f"Validation failed due to error: {str(e)}"
def run_validation():
    validator = PositiveNumberValidator()
    test_cases = [
        "123",
        "+45.67",
        "-890",
        "",
        "abc",
        "  789  ",
        None,
        12345,
        -0.001
    ]
    print("=== Positive Number Validation Results ===\n")
    for test_case in test_cases:
        result = validator.validate_positive_number(test_case)
        if isinstance(result, bool):
            status = "VALID" if result else "INVALID"
        elif isinstance(result, str):
            status = f"ERROR: {result}"
        print(f"Input: {repr(test_case)} | Status: {status}")
if __name__ == '__main__':
    run_validation()