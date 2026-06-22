import re

def is_valid_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

if __name__ == '__main__':
    test_emails = [
        "user@example.com",
        "invalid.email@",
        "another.user@domain.org",
        "bad@.com",
        "good.email+tag@sub.domain.co.uk",
        "@missing-local.com",
        "spaces in@email.com"
    ]
    for email in test_emails:
        print(is_valid_email(email))