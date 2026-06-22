import re

EMAIL_PATTERN = re.compile(
    r"^(?P<local>[a-zA-Z0-9._%+-]+)"
    r"@"
    r"(?P<domain>[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$"
)

def validate_email(email):
    if not isinstance(email, str):
        return False
    if not email:
        return False
    if EMAIL_PATTERN.match(email):
        return True
    return False

if __name__ == "__main__":
    test_cases = [
        "user@example.com",
        "user.name+tag@sub.domain.co.uk",
        "invalid-email@",
        "@domain.com",
        "missing-at-sign.com",
        "spaces in local @domain.com",
        "valid123@test.org"
    ]
    
    results = []
    for email in test_cases:
        results.append(validate_email(email))
    
    for i, result in enumerate(results):
        print(f"{test_cases[i]}: {result}")