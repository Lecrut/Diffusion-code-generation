import re

def validate_international_dialing_code(code):
    if not isinstance(code, str):
        raise TypeError("Input must be a string")
    if not code:
        raise ValueError("Input string must not be empty")
    pattern = r'^\+[1-9]\d{1,14}$'
    match = re.match(pattern, code)
    if not match:
        raise ValueError(f"'{code}' does not conform to international dialing code structure")
    return code.strip()

if __name__ == '__main__':
    valid_codes = ["+1", "+44", "+86", "+123456789012345"]
    invalid_codes = ["+0", "+abc", "123", "+", "+007", ""]
    results = []
    for code in valid_codes:
        results.append(validate_international_dialing_code(code))
    for code in invalid_codes:
        try:
            validate_international_dialing_code(code)
            results.append("INVALID")
        except (TypeError, ValueError):
            results.append("INVALID")
    for result in results:
        print(result)