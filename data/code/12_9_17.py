import re

DIALING_CODE_PATTERN = re.compile(r"^\+\d{1,15}$")

class DialingCodeValidator:
    def validate(self, code):
        if not isinstance(code, str):
            raise TypeError("Input must be a string")
        if not DIALING_CODE_PATTERN.match(code):
            raise ValueError("Invalid international dialing code format")
        if code[1:].isdigit() and int(code[1:]) > 0:
            return True
        raise ValueError("Dialing code cannot start with zero")

if __name__ == '__main__':
    validator = DialingCodeValidator()
    samples = [
        "+1",
        "+44",
        "+86",
        "+123456789012345",
        "+01",
        "1",
        "+",
        "+abc",
        "+9999999999999999",
        123
    ]
    results = []
    for sample in samples:
        try:
            outcome = validator.validate(sample)
            results.append(f"Valid: {sample} -> {outcome}")
        except Exception as exc:
            results.append(f"Invalid: {sample} -> {exc}")
    for result_line in results:
        print(result_line)