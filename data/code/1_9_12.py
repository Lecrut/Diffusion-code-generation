import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

if __name__ == '__main__':
    test_emails = [
        "user@example.com",
        "invalid.email@com",
        "another.user+tag@domain.co.uk",
        "bad@@domain.com",
        "missing-at-sign.com",
        "user@.com",
        "user@com"
    ]
    for email in test_emails:
        print(f"{email}: {validate_email(email)}")