def validate_phone_number(phone: str) -> bool:
    if not (7 <= len(phone) <= 15):
        return False
    for char in phone:
        if char.isalpha():
            return False
    return True

if __name__ == '__main__':
    test_cases = ["1234567", "123456789012345", "1234567890123456", "abc123", "12-34-56"]
    results = [validate_phone_number(case) for case in test_cases]
    for case, result in zip(test_cases, results):
        print(result)