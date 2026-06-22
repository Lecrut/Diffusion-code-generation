import re

email_pattern = re.compile(
    r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
)

def validate_email(email: str) -> bool:
    if email_pattern.match(email):
        return True
    return False

if __name__ == '__main__':
    test_emails = [
        "user@example.com",
        "john.doe@domain.org",
        "invalid-email",
        "@missing-local.com",
        "no-at-sign.com",
        "double@@.com",
        "user@.com",
        "user@com",
        "user@sub.domain.com"
    ]

    results = [validate_email(email) for email in test_emails]
    print(results)