import re

_EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

def validate_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    return bool(_EMAIL_REGEX.match(email))

if __name__ == '__main__':
    test_cases = [
        ("user@example.com", True),
        ("first.last@domain.co.uk", True),
        ("user+tag@domain.org", True),
        ("user_name@sub.domain.com", True),
        ("invalid@", False),
        ("@example.com", False),
        ("user", False),
        ("user@.com", False),
        ("user@domain..com", False),
        ("double..dots@domain.com", False),
        ("", False),
        (None, False),
        (123, False),
        ("user@domain", False),
    ]

    results = [
        {"email": email, "expected": expected, "actual": validate_email(email), "pass": validate_email(email) == expected}
        for email, expected in test_cases
    ]
    print(results)