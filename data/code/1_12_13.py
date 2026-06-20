import re

EMAIL_REGEX = re.compile(
    r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"
)

def validate_email(email: str) -> bool:
    return bool(email and EMAIL_REGEX.match(email))

if __name__ == '__main__':
    test_emails = [
        "user@example.com",
        "invalid.email",
        "user@.com",
        "user@exam ple.com",
        "valid+tag@domain.co.uk",
        "",
        "no@no",
    ]
    results = [validate_email(email) for email in test_emails]
    print(results)