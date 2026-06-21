import re

def validate_international_dialing_code(code: str) -> bool:
    assert isinstance(code, str), "Input must be a string"
    pattern = r"^\+[1-9]\d{0,12}$"
    return bool(re.match(pattern, code))

if __name__ == '__main__':
    sample_codes = [
        "+1",
        "+44",
        "+81",
        "+86",
        "+7",
        "+1234567890123",
        "+0",
        "44",
        "+123abc",
        "+",
        "+12 34"
    ]
    results = []
    for code in sample_codes:
        result = validate_international_dialing_code(code)
        results.append((code, result))
    for code, is_valid in results:
        print(f"{code}: {is_valid}")