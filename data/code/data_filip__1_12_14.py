import re

EMAIL_PATTERN = re.compile(
    r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"
)

def is_valid_email(email: str) -> bool:
    return bool(EMAIL_PATTERN.fullmatch(email))

if __name__ == '__main__':
    test_emails = [
        "user@example.com",
        "invalid.email",
        "user@.com",
        "user@com",
        "user+tag@example.org",
        "",
        "@example.com",
        "user@localhost",
    ]
    results = {email: is_valid_email(email) for email in test_emails}
    for email, valid in results.items():
        print(f"{email!r}: {valid}")