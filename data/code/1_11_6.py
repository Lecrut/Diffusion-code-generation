import re

def validate_email(email: str) -> bool:
    pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    return bool(pattern.match(email))

if __name__ == '__main__':
    sample_emails = [
        "user@example.com",
        "invalid.email",
        "test.user@domain.org",
        "bad@.com",
        "another@test.co.uk"
    ]
    for email in sample_emails:
        result = validate_email(email)
        print(f"{email}: {result}")