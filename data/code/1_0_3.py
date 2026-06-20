import re

VALID_EMAIL_PATTERN = re.compile(
    r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
)

def validate_email(email: str) -> bool:
    return bool(VALID_EMAIL_PATTERN.match(email))

def main():
    test_emails = [
        "user@example.com",
        "invalid.email",
        "another.user@domain.org",
        "bad@.com",
        "test@sub.domain.co.uk"
    ]
    results = {email: validate_email(email) for email in test_emails}
    print(results)

if __name__ == '__main__':
    main()