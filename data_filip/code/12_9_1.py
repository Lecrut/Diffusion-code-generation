import re

def validate_dialing_code(code):
    if not isinstance(code, str):
        raise TypeError("Input must be a string")
    pattern = r'^[+]?[1-9]\d{1,14}$'
    if not re.match(pattern, code):
        raise ValueError(f"'{code}' is not a valid international dialing code")
    return True

if __name__ == '__main__':
    test_cases = [
        "+1",
        "+44",
        "+86",
        "+123456789012345",
        "+01",
        "1",
        "+",
        "+abc",
        "+12 34",
        123,
        None,
        "+331",
        "+919876543210"
    ]
    for test in test_cases:
        try:
            result = validate_dialing_code(test)
            print(f"{repr(test)}: {result}")
        except Exception as e:
            print(f"{repr(test)}: {type(e).__name__}: {e}")