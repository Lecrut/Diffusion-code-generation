import re

def validate_international_dialing_code(code: str) -> bool:
    if not isinstance(code, str):
        raise TypeError("Input must be a string")
    pattern = r'^\+?[1-9]\d{1,14}$'
    return bool(re.match(pattern, code))

if __name__ == '__main__':
    sample_values = ["+1", "+123456789012345", "+91", "invalid", "+0", "+123abc"]
    for val in sample_values:
        print(f"validate_international_dialing_code('{val}') = {validate_international_dialing_code(val)}")