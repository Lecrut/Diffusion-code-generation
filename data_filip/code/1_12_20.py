import re

_EMAIL_REGEX = re.compile(
    r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
)

def validate_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    return _EMAIL_REGEX.match(email) is not None

if __name__ == '__main__':
    sample_emails = [
        "user@example.com",
        "invalid.email",
        "@missing.com",
        "no_at_sign",
        "valid+tag@sub.domain.org",
        "spaces in@email.com",
        "a@b.c",
    ]

    results = [validate_email(e) for e in sample_emails]
    print(results)