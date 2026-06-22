import re

def is_valid_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

if __name__ == '__main__':
    test_cases = [
        "user@example.com",
        "invalid-email",
        "@missing-local.com",
        "missing-at-sign.com",
        "user.name+tag@domain.co.uk",
        "spaces in@email.com",
        "user@domain",
        "valid123@test-domain.org"
    ]
    results = [is_valid_email(email) for email in test_cases]
    print(results)