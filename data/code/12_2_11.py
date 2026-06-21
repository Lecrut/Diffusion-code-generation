def is_valid_phone_number(phone_number: str) -> bool:
    allowed_characters = set('0123456789 ()-')
    return all(char in allowed_characters for char in phone_number)

if __name__ == '__main__':
    sample_numbers = [
        "123-456-7890",
        "(123) 456-7890",
        "1234567890",
        "123-456-7890x123",
        "(123) 456-7890 ext. 123",
        "",
        "123 456 7890",
        "123-456-7890!",
        "(123)-456-7890",
        "abc-def-ghij"
    ]

    for number in sample_numbers:
        print(f"Number: {number!r}, Valid: {is_valid_phone_number(number)}")