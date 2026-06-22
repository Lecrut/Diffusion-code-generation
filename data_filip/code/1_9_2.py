import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

if __name__ == '__main__':
    test_emails = [
        "user@example.com",
        "invalid-email@",
        "another.user@domain.co.uk",
        "bad@@email.com",
        "test@domain.123",
        "valid.email+tag@sub.domain.org",
        "@missing-local.com",
        "no-at-sign.com",
        "spaces in@email.com",
        "valid123@test-domain.net"
    ]
    results = [validate_email(email) for email in test_emails]
    for email, result in zip(test_emails, results):
        print(f"{email}: {result}")