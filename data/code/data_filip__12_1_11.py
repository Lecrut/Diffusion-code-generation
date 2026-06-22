def validate_phone_number(phone: str) -> str:
    digits_only = ''.join(char for char in phone if char.isdigit())
    is_valid = len(digits_only) == 11
    return f"Cleaned: {digits_only}, Valid: {is_valid}"

if __name__ == '__main__':
    sample_numbers = ["+1 (555) 123-4567", "12345678901", "555-abc-1234"]
    for num in sample_numbers:
        print(validate_phone_number(num))