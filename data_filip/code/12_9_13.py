import re

PATTERN = re.compile(r'^\+[1-9]\d{1,14}$')

def validate_international_dialing_code(code: str) -> str:
    if not isinstance(code, str):
        raise TypeError(f"Expected string, got {type(code).__name__}")
    if not code:
        raise ValueError("Input string cannot be empty")
    if not PATTERN.match(code):
        raise ValueError(f"'{code}' does not conform to international dialing code structure")
    return code

if __name__ == '__main__':
    valid_samples = [
        "+1",
        "+44",
        "+86",
        "+91",
        "+123456789012345",
        "+4930123456"
    ]
    
    invalid_samples = [
        "123",
        "+0",
        "+abc",
        "",
        "+",
        123,
        "+1234567890123456"
    ]
    
    for sample in valid_samples:
        result = validate_international_dialing_code(sample)
        print(result)
        
    for sample in invalid_samples:
        try:
            validate_international_dialing_code(sample)
        except (TypeError, ValueError) as e:
            print(str(e))