import re

EMAIL_PATTERN = re.compile(
    r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
)

def validate_email(email):
    return bool(EMAIL_PATTERN.match(email))

def validate_emails(emails):
    return [validate_email(email) for email in emails]

if __name__ == '__main__':
    test_emails = [
        "user@example.com",
        "invalid.email@",
        "@missing-local.com",
        "user@.com",
        "user@com",
        "user_name+tag@domain.co.uk",
        "spaces in@email.com",
        "user@domain.c",
        "valid.email.name@sub.domain.com",
        "",
        "justtext"
    ]
    results = validate_emails(test_emails)
    print(results)