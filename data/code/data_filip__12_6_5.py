def validate_phone_number(phone):
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
    test_cases = ["1234567", "123-456-7890", "123456789012345", "123456", "1234567890123456", "abc123", "123abc456"]
    results = {}
    for case in test_cases:
        results[case] = validate_phone_number(case)
    print(results)