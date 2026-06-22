def validate_phone_number(phone_number):
    if not isinstance(phone_number, str):
        return False
    if len(phone_number) < 7 or len(phone_number) > 15:
        return False
    if any(char.isalpha() for char in phone_number):
        return False
    return True

if __name__ == '__main__':
    sample_numbers = [
        "1234567",
        "123456789012345",
        "123-456-7890",
        "123 456 7890",
        "123456",
        "1234567890123456",
        "123a4567",
        "abcdefghi",
        "1234567890",
        "+12345678901234",
        "",
        "123-abc-7890"
    ]
    for number in sample_numbers:
        print(validate_phone_number(number))