import re

EMAIL_PATTERN = re.compile(
    r'^[a-zA-Z0-9.!#$%&\'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$'
)

def validate_email(email):
    return bool(EMAIL_PATTERN.match(email))

if __name__ == '__main__':
    test_emails = [
        "user@example.com",
        "invalid-email@",
        "@missing-local.com",
        "user.name+tag@domain.co.uk",
        "bad@.com",
        "spaces in@email.com",
        "valid123@sub.domain.org",
        "a@b"
    ]
    for email in test_emails:
        result = validate_email(email)
        print(result)