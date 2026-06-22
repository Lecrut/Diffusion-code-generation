import re

EMAIL_PATTERN = re.compile(
    r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
)

def validate_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    return EMAIL_PATTERN.match(email) is not None

if __name__ == '__main__':
    test_cases = [
        ("user@example.com", True),
        ("invalid.email", False),
        ("@missinglocal.com", False),
        ("noat.com", False),
        ("valid+tag@sub.domain.co.uk", True),
        ("spaces in@email.com", False),
        ("", False),
        ("double@@dot.com", False),
    ]

    results = {}
    for email, expected in test_cases:
        is_valid = validate_email(email)
        results[email] = is_valid

    print(results)