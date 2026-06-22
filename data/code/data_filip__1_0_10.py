import re

VALID_EMAIL_PATTERN = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

def is_valid_email(email: str) -> bool:
    if not email or not isinstance(email, str):
        return False
    return bool(VALID_EMAIL_PATTERN.match(email))

if __name__ == '__main__':
    test_emails = [
        "user@example.com",
        "user.name+tag@sub.domain.org",
        "invalid-email@",
        "@missing-local.com",
        "no-at-symbol.com",
        "user@invalid-domain",
        "another.valid-email@co.uk"
    ]
    results = {email: is_valid_email(email) for email in test_emails}
    for email, is_valid in results.items():
        print(email, is_valid)