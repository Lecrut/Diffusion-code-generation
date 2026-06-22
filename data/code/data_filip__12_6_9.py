def validate_phone_number(phone_number):
    if not isinstance(phone_number, str):
        return False
    if len(phone_number) < 7 or len(phone_number) > 15:
        return False
    if any(c.isalpha() for c in phone_number):
        return False
    return True

if __name__ == '__main__':
    sample_numbers = [
        "1234567",
        "123-456-7890",
        "12345",
        "1234567890123456",
        "123a567",
        "+1-123-456-7890",
        "123 456 7890",
        "0000000"
    ]
    for number in sample_numbers:
        result = validate_phone_number(number)
        print(result)