import re

EMAIL_REGEX = re.compile(
    r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"
)

def validate_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    return bool(EMAIL_REGEX.match(email))

if __name__ == '__main__':
    test_cases = [
        ("user@example.com", True),
        ("first.last@sub.domain.co", True),
        ("invalid@.com", False),
        ("invalid@com.", False),
        ("@missing-local.com", False),
        ("no-at-sign.com", False),
        ("spaces in@email.com", False),
        ("simple@example.org", True),
        ("valid+tag@example.org", True),
        ("user.name@domain.com", True),
        ("user@domain.com.", False),
        ("user@..com", False),
        ("user@com", False),
        ("", False),
    ]

    results = []
    for email, expected in test_cases:
        is_valid = validate_email(email)
        results.append((email, is_valid))
    
    for email, is_valid in results:
        print(f"{email}: {is_valid}")