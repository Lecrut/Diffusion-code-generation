import re

PHONE_PATTERN = re.compile(
    r"^(?:\+?1[-\s]?)?"
    r"\(?\d{3}\)?[-\s]?"
    r"\d{3}[-\s]?"
    r"\d{4}$"
)

def validate_phone(phone: str) -> bool:
    if not isinstance(phone, str):
        return False
    return bool(PHONE_PATTERN.match(phone))

if __name__ == "__main__":
    test_cases = [
        ("1234567890", True),
        ("(123) 456-7890", True),
        ("123-456-7890", True),
        ("123.456.7890", False),
        ("123456789", False),
        ("12345678901", False),
        ("+1 (123) 456-7890", True),
        ("1-123-456-7890", True),
        ("123 456 7890", True),
        ("abc-def-ghij", False),
        ("", False),
    ]

    for phone, expected in test_cases:
        result = validate_phone(phone)
        print(f"{result}")