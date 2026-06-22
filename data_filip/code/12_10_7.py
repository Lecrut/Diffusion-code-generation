import re

def validate_phone(phone):
    pattern = re.compile(r'^(\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$')
    return bool(pattern.match(phone))

if __name__ == '__main__':
    test_numbers = [
        "1234567890",
        "123-456-7890",
        "123.456.7890",
        "(123) 456-7890",
        "123 456 7890",
        "1-123-456-7890",
        "+1-123-456-7890",
        "123456789",
        "12345678901",
        "abc-def-ghij",
        "123-45-6789"
    ]
    results = [validate_phone(num) for num in test_numbers]
    for num, res in zip(test_numbers, results):
        print(f"{res}")