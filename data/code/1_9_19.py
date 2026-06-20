import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

if __name__ == '__main__':
    test_emails = [
        "user@example.com",
        "invalid-email",
        "user.name@domain.co.uk",
        "@missing-local.com",
        "no-at-sign.com",
        "user@.invalid",
        "user@domain.",
        "a@b.c",
        "valid_email+tag@sub.domain.org"
    ]
    for email in test_emails:
        print(f"{email}: {is_valid_email(email)}")