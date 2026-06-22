import re
import sys

_email_regex = re.compile(r"^(?:[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)$")

def validate_email(email):
    if not isinstance(email, str):
        return False
    if len(email) > 254:
        return False
    if "@" not in email:
        return False
    return _email_regex.match(email) is not None

if __name__ == '__main__':
    test_cases = [
        "user@example.com",
        "invalid.email",
        "test@domain.org",
        "@missing.local",
        "no-at-sign.com"
    ]
    for case in test_cases:
        print(f"{case}: {validate_email(case)}")