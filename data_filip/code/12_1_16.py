def validate_phone_number(phone_number: str) -> bool:
    digits = ''.join(char for char in phone_number if char.isdigit())
    return len(digits) == 11

if __name__ == '__main__':
    sample_numbers = [
        "12345678901",
        "+1-234-567-8901",
        "(123) 456-7890",
        "1234567890",
        "abc123def456ghi789j01k",
        "123456789012",
        ""
    ]
    for number in sample_numbers:
        result = validate_phone_number(number)
        print(result)