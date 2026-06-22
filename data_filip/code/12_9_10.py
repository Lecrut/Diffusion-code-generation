import re

def validate_international_dialing_code(code: str) -> bool:
    assert isinstance(code, str), "Input must be a string"
    pattern = r'^\+[1-9]\d{0,12}$'
    return bool(re.match(pattern, code))

if __name__ == '__main__':
    samples = ["+1", "+44", "+86", "+91", "+1234567890", "+01", "+abc", "123", "+1 ", " +1", "+", "+0", "+1234567890123"]
    results = [validate_international_dialing_code(s) for s in samples]
    print(results)