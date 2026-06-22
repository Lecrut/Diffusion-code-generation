def is_valid_phone_number(phone_number):
    allowed_characters = set('0123456789 -()')
    return all(char in allowed_characters for char in phone_number)

if __name__ == '__main__':
    sample_values = [
        "123-456-7890",
        "(123) 456-7890",
        "1234567890",
        "123-456-7890!",
        "abc-def-ghij",
        "",
        "+1 (555) 123-4567",
        "123 456 7890"
    ]
    for value in sample_values:
        print(is_valid_phone_number(value))