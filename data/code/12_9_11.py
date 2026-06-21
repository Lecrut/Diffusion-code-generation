import re
import typing

def validate_international_dialing_code(code: str) -> bool:
    if not isinstance(code, str):
        raise TypeError("Input must be a string")
    if not code:
        return False
    pattern = r"^\+\d{1,3}$"
    if not re.match(pattern, code):
        return False
    numeric_part = code[1:]
    if numeric_part.startswith('0'):
        return False
    if len(numeric_part) > 3:
        return False
    return True

if __name__ == '__main__':
    sample_codes = [
        "+1",
        "+44",
        "+86",
        "+12345",
        "123",
        "+",
        "+01",
        "abc",
        "",
        "+55",
    ]

    for sample in sample_codes:
        result = validate_international_dialing_code(sample)
        print(result)