def is_valid_phone_number(phone):
    allowed_chars = set("0123456789- ()")
    return all(char in allowed_chars for char in phone) and len(phone) > 0

if __name__ == '__main__':
    sample_numbers = [
        "123-456-7890",
        "(555) 123-4567",
        "123 456 7890",
        "555.123.4567",
        "abc123",
        "123-456-7890!",
        "",
        "0"
    ]
    for number in sample_numbers:
        print(f"{number}: {is_valid_phone_number(number)}")