def validate_phone_number(phone_number: str) -> bool:
    if not isinstance(phone_number, str):
        return False
    if len(phone_number) < 7 or len(phone_number) > 15:
        return False
    for char in phone_number:
        if char.isalpha():
            return False
    return True

if __name__ == '__main__':
    test_numbers = ["1234567", "123-456-7890", "123456789012345", "123456", "abc123", "+1234567890"]
    for number in test_numbers:
        result = validate_phone_number(number)
        print(f"{number}: {result}")