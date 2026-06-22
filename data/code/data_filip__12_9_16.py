import re

def validate_international_dialing_code(code: str) -> bool:
    if not isinstance(code, str):
        raise TypeError("Input must be a string.")
    pattern = r'^\+?[1-9]\d{1,14}$'
    if not re.match(pattern, code):
        raise ValueError("Invalid international dialing code format.")
    return True

if __name__ == '__main__':
    test_code = "+12025550199"
    result = validate_international_dialing_code(test_code)
    print(result)