def validate_phone_number(phone_number):
    allowed_characters = set('0123456789 -()')
    return all(char in allowed_characters for char in phone_number) and len(phone_number) > 0

if __name__ == '__main__':
    samples = [
        "123-456-7890",
        "(123) 456-7890",
        "123 456 7890",
        "1234567890",
        "123-456-7890x",
        "",
        "123 456 7890!",
        "(123)456-7890",
        "abc-def-ghij"
    ]
    for sample in samples:
        print(validate_phone_number(sample))