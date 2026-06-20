import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

if __name__ == '__main__':
    test_emails = [
        "user@example.com",
        "invalid.email",
        "user@.com",
        "user@com",
        "user.name+tag@domain.co.uk",
        "@missing.com",
        "spaces@in email.com",
        "user@domain.123"
    ]
    for email in test_emails:
        result = is_valid_email(email)
        print(f"{email}: {result}")