import re

EMAIL_REGEX = re.compile(
    r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"
)

def validate_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    if len(email) > 254:
        return False
    return EMAIL_REGEX.match(email) is not None

if __name__ == '__main__':
    test_emails = [
        "user@example.com",
        "name.surname@sub.domain.org",
        "invalid@",
        "@missing.com",
        "spaces @example.com",
        "user@-invalid.com",
        "user@.invalid.com",
        "user@invalid-.com",
        "plainaddress",
        "user@localdomain"
    ]

    results = [validate_email(email) for email in test_emails]
    print(results)