import re

_EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

def is_valid_email(email):
    if not isinstance(email, str):
        return False
    return bool(_EMAIL_PATTERN.match(email))

if __name__ == '__main__':
    test_emails = [
        "user@example.com",
        "invalid.email",
        "@missing-local.com",
        "plainaddress",
        "user+tag@domain.co.uk",
        "user name@example.com"
    ]
    results = [is_valid_email(e) for e in test_emails]
    print(results)