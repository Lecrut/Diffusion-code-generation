import re

_email_pattern = re.compile(
    r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
)

def validate_email(email: str) -> bool:
    if not email or not isinstance(email, str):
        return False
    return bool(_email_pattern.match(email))

if __name__ == '__main__':
    sample_emails = [
        "user@example.com",
        "invalid.email",
        "test+tag@sub.domain.org",
        "@missing-local.com",
        "no-at-sign.com",
        "user@.com",
        "user@domain..com",
        "spaces in@email.com",
        "plainaddress",
        "u@b.c"
    ]

    for email in sample_emails:
        result = validate_email(email)
        print(f"{email}: {result}")