import re

_PATTERN = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

def validate_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    return bool(_PATTERN.match(email))

if __name__ == '__main__':
    test_emails = [
        "user@example.com",
        "invalid.email",
        "test@domain.co.uk",
        "bad@.com",
        "no_at_sign.com",
        "valid+tag@sub.domain.org"
    ]
    for email in test_emails:
        print(validate_email(email))