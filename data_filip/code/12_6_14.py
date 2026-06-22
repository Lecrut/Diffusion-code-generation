def validate_phone_number(phone):
    if not isinstance(phone, str):
        return False
    if len(phone) < 7 or len(phone) > 15:
        return False
    for char in phone:
        if char.isalpha():
            return False
    return True

if __name__ == '__main__':
    test_cases = ["1234567", "123456789012345", "1234567890123456", "abc123", "12-34-56-78", "123456"]
    for test in test_cases:
        result = validate_phone_number(test)
        print(f"{test}: {result}")