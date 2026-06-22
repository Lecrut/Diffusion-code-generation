import re

def validate_phone(phone: str) -> bool:
    pattern = re.compile(r'^(\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$')
    if phone is None:
        return False
    return bool(pattern.match(phone))

if __name__ == '__main__':
    test_cases = [
        "1234567890",
        "(123) 456-7890",
        "123-456-7890",
        "+1-123-456-7890",
        "123.456.7890",
        "123456789",
        "1234567890123",
        None,
        "abc-def-ghij",
        "1 (123) 456-7890"
    ]

    results = [validate_phone(tc) for tc in test_cases]
    print(results)