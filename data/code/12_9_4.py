import re

def validate_international_dialing_code(code: str) -> bool:
    if not isinstance(code, str):
        raise TypeError("Input must be a string")
    pattern = r'^\+\d{1,3}$'
    if not re.match(pattern, code):
        return False
    numeric_part = code[1:]
    if not numeric_part.isdigit():
        return False
    length = len(numeric_part)
    if length < 1 or length > 3:
        return False
    return True

if __name__ == '__main__':
    samples = ["+1", "+44", "+86", "+999", "+1234", "+12a", "123", "+", "abc", "+001"]
    results = {sample: validate_international_dialing_code(sample) for sample in samples}
    for sample, result in results.items():
        print(f"{sample}: {result}")