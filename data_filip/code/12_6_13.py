def validate_phone_number(phone_number: str) -> bool:
    if not isinstance(phone_number, str):
        return False
    length = len(phone_number)
    if length < 7 or length > 15:
        return False
    for char in phone_number:
        if char.isalpha():
            return False
    return True

if __name__ == '__main__':
    test_numbers = [
        "1234567",
        "123-456-7890",
        "+123456789012345",
        "abcdefghi",
        "123",
        "1234567890123456",
        "12345678",
        "1-800-555-0199"
    ]
    results = [validate_phone_number(num) for num in test_numbers]
    print(results)