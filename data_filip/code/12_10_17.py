import re

_pattern = re.compile(r'^(\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$')

def validate_phone(phone: str) -> bool:
    return bool(_pattern.match(phone))

if __name__ == '__main__':
    test_cases = [
        ("1234567890", True),
        ("123-456-7890", True),
        ("(123) 456-7890", True),
        ("1-123-456-7890", True),
        ("+1 123 456 7890", True),
        ("123456789", False),
        ("12345678901234", False),
        ("abc-def-ghij", False),
        ("(123)456-789", False),
        ("123 456 7890", True),
    ]
    results = []
    for phone, expected in test_cases:
        result = validate_phone(phone)
        results.append((phone, result, expected))
        print(result)