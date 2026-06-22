import re

EMAIL_REGEX = re.compile(
    r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
)

def validate_email(email: str) -> bool:
    return bool(EMAIL_REGEX.match(email))

if __name__ == '__main__':
    test_cases = [
        ("user@example.com", True),
        ("john.doe@company.co.uk", True),
        ("invalid@", False),
        ("@missing.com", False),
        ("no-at-sign.com", False),
        ("double@@at.com", False),
        ("spaces in@email.com", False),
        ("user@.com", False),
        ("user@com.", False),
        ("plainaddress", False),
        ("user@domain..com", False),
        ("a@b.c", False),
        ("valid+tag@email.org", True),
        ("user%domain.com@example.com", True),
        ("", False),
    ]

    results = [(email, validate_email(email)) for email, _ in test_cases]
    print(results)