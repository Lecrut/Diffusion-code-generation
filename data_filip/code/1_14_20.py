import re

def validate_email(email):
    pattern = re.compile(
        r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    )
    return bool(pattern.match(email))

if __name__ == '__main__':
    test_cases = [
        ("user@example.com", True),
        ("john.doe+tag@sub.domain.org", True),
        ("invalid@", False),
        ("@missing-local.com", False),
        ("no-at-sign.com", False),
        ("user@.com", False),
        ("user@com", False),
        ("spaces in@email.com", False),
        ("valid.email@domain.co.uk", True),
        ("a@b.c", False),
    ]
    results = []
    for email, expected in test_cases:
        result = validate_email(email)
        results.append((email, expected, result))
    for email, expected, result in results:
        print(f"{email}: expected={expected}, got={result}, match={expected == result}")