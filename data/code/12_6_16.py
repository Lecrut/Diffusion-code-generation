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
    sample_numbers = [
        "1234567",
        "123-456-7890",
        "123456789012345",
        "123456",
        "1234567890123456",
        "1234567abc",
        "9876543210"
    ]
    for number in sample_numbers:
        result = validate_phone_number(number)
        print(result)