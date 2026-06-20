import re

email_pattern = re.compile(
    r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
)

def validate_email(email):
    return bool(email_pattern.match(email))

if __name__ == '__main__':
    valid_emails = [
        "user@example.com",
        "first.last@domain.org",
        "user+tag@sub.domain.co.uk"
    ]
    invalid_emails = [
        "user@.com",
        "@example.com",
        "user@example",
        "user@@example.com",
        "user@example.c"
    ]
    results = {
        "valid": [validate_email(e) for e in valid_emails],
        "invalid": [validate_email(e) for e in invalid_emails]
    }
    print(results)