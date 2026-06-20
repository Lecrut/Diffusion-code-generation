import re

def validate_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

if __name__ == '__main__':
    test_emails = [
        "user@example.com",
        "invalid.email",
        "user.name+tag@domain.co.uk",
        "@missing-local.com",
        "no-at-sign.com",
        "user@.com",
        "user@domain",
        "spaces in@domain.com",
        "valid_email@sub.domain.org"
    ]
    results = [validate_email(e) for e in test_emails]
    print(list(zip(test_emails, results)))