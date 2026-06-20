import re

def is_valid_email(email: str) -> bool:
    pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    return bool(pattern.match(email))

if __name__ == '__main__':
    test_emails = [
        "user@example.com",
        "john.doe@subdomain.example.co.uk",
        "invalid-email",
        "@missing-local.com",
        "no-at-sign.com",
        "user@.com",
        "user@domain",
        "spaces in@email.com",
        "user@@domain.com",
        "simple@example.org"
    ]
    results = [is_valid_email(email) for email in test_emails]
    for email, valid in zip(test_emails, results):
        print(f"{email}: {valid}")