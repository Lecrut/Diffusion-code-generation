import re

def validate_international_dialing_code(code: str) -> bool:
    if not isinstance(code, str):
        raise TypeError("Input must be a string")
    pattern = r'^\+[1-9]\d{0,12}$'
    return bool(re.match(pattern, code))

if __name__ == '__main__':
    sample_codes = [
        "+1",
        "+44",
        "+86",
        "+7",
        "+91",
        "+123456789012",
        "+01",
        "+abc",
        "123",
        "+",
        "+1234567890123",
        ""
    ]
    for sample in sample_codes:
        result = validate_international_dialing_code(sample)
        print(f"{sample}: {result}")