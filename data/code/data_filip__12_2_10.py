def is_valid_phone_number(phone_number):
    allowed_characters = set('0123456789 ()-')
    return all(char in allowed_characters for char in phone_number) and len(phone_number) > 0

if __name__ == '__main__':
    sample_numbers = [
        "123-456-7890",
        "(123) 456-7890",
        "123 456 7890",
        "123-456-7890x",
        "abc-123-4567",
        "",
        "123_456_7890"
    ]
    for number in sample_numbers:
        print(is_valid_phone_number(number))