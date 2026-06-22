import re
import sys

_email_pattern = re.compile(
    r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
)

def validate_email(email):
    if not isinstance(email, str):
        return False
    return bool(_email_pattern.match(email))

if __name__ == '__main__':
    test_emails = [
        "user@example.com",
        "invalid.email@com",
        "another.valid@test.co.uk",
        "no-at-symbol.com",
        12345
    ]
    for email in test_emails:
        result = validate_email(email)
        print(f"{email}: {result}")