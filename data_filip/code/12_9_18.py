import re

def validate_international_dialing_code(code: str) -> bool:
    if not isinstance(code, str):
        raise TypeError("Input must be a string")
    pattern = r'^\+\d{1,3}\s?\d{1,14}$'
    return bool(re.match(pattern, code))

if __name__ == '__main__':
    samples = [
        "+1 2025551234",
        "+44 20 7946 0958",
        "+86 10 12345678",
        "+12025551234",
        "12025551234",
        "+",
        "+1",
        "+12345678901234567",
        "+1 202-555-1234",
        ""
    ]
    results = [validate_international_dialing_code(s) for s in samples]
    print(dict(zip(samples, results)))