import re
import sys

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

def validate_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    return bool(EMAIL_REGEX.match(email))

if __name__ == '__main__':
    sample_emails = [
        "user@example.com",
        "invalid.email",
        "@missing.com",
        "no-at-sign.com",
        "user@.com",
        "user@sub.domain.com",
        "UPPERCASE@EXAMPLE.COM"
    ]
    results = [validate_email(email) for email in sample_emails]
    print(results)