import re

_email_regex = re.compile(
    r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
)

def validate_email(email: str) -> bool:
    return bool(_email_regex.match(email))

if __name__ == '__main__':
    test_emails = [
        "user@example.com",
        "invalid.email",
        "test+tag@domain.co.uk",
        "no-at-sign.com",
        "@missing-local.com",
        "spaces in@email.com",
        "valid_user@sub.domain.example.org"
    ]

    results = [(email, validate_email(email)) for email in test_emails]
    print(results)