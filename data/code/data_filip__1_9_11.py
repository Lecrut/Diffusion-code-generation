import re

def is_valid_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

if __name__ == '__main__':
    test_emails = [
        "user@example.com",
        "invalid.email",
        "missing@domain",
        "name+tag@sub.domain.org",
        "@nodomain.com",
        "no_at_sign",
        "user@.com",
        "user@domain..com",
        "user name@domain.com",
        "user@domain.c"
    ]
    results = [is_valid_email(email) for email in test_emails]
    for email, valid in zip(test_emails, results):
        print(f"{email}: {valid}")