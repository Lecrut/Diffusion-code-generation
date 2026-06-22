import re

EMAIL_PATTERN = re.compile(
    r"^(?P<local>[a-zA-Z0-9_.+-]+)@"
    r"(?P<domain>[a-zA-Z0-9-]+)"
    r"(?:\.(?P<tld>[a-zA-Z]{2,}))+$"
)

def validate_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    return EMAIL_PATTERN.match(email) is not None

if __name__ == '__main__':
    test_cases = [
        "user@example.com",
        "user.name+tag@sub.domain.co.uk",
        "invalid-email@",
        "@missing-local.com",
        "no-at-symbol.com",
        "spaces in @email.com",
        "valid@domain123.org",
        "short@a.b"
    ]
    results = []
    for case in test_cases:
        results.append((case, validate_email(case)))
    print(results)