def validate_phone_number(phone_number):
    allowed_characters = set('0123456789 -()')
    return all(char in allowed_characters for char in phone_number)

if __name__ == '__main__':
    samples = [
        "123-456-7890",
        "(123) 456-7890",
        "123 456 7890",
        "123-456-7890 ext 123",
        "abc-def-ghij",
        "123 456 7890!",
        "",
        "(123)456-7890",
        "+1234567890",
        "123-456-7890 x123"
    ]
    for sample in samples:
        print(validate_phone_number(sample))