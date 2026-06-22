def validate_phone_number(phone: str) -> bool:
    if not isinstance(phone, str):
        return False
    
    length = len(phone)
    if length < 7 or length > 15:
        return False
    
    for char in phone:
        if char.isalpha():
            return False
            
    return True

if __name__ == '__main__':
    test_cases = [
        ("1234567", True),
        ("123456", False),
        ("1234567890123456", False),
        ("123456789012345", True),
        ("123-456-7890", True),
        ("123 456 7890", True),
        ("abc1234567", False),
        ("+1234567890", True),
        ("123456789012345", True),
        ("12345", False)
    ]
    
    for phone, expected in test_cases:
        result = validate_phone_number(phone)
        print(f"{phone!r:20} -> {result} (expected: {expected})")