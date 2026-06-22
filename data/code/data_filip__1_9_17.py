import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

if __name__ == '__main__':
    sample_emails = [
        "user@example.com",
        "invalid.email@",
        "test.name+tag@domain.co.uk",
        "@missing-local.com",
        "no-at-sign.com",
        "spaces in@email.com",
        "user@.com",
        "user@domain.c",
        "valid.email_123@sub.domain.org"
    ]
    for email in sample_emails:
        result = validate_email(email)
        print(result)