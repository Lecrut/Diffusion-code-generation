import re

def validate_phone(phone: str) -> bool:
    pattern = re.compile(r'^(\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$')
    return bool(pattern.fullmatch(phone))

if __name__ == '__main__':
    test_numbers = [
        "1234567890",
        "123-456-7890",
        "123.456.7890",
        "(123) 456-7890",
        "1-123-456-7890",
        "+1-123-456-7890",
        "123-45-6789",
        "123456789",
        "12345678901",
        "abc-def-ghij",
        "123 456 7890"
    ]
    for number in test_numbers:
        result = validate_phone(number)
        print(result)