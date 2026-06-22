import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

if __name__ == '__main__':
    test_emails = [
        "user@example.com",
        "invalid-email",
        "user.name+tag@domain.co.uk",
        "@missing-local.com",
        "no-at-sign.com",
        "spaces in@email.com",
        "valid123@sub.domain.org"
    ]
    results = [validate_email(email) for email in test_emails]
    for email, valid in zip(test_emails, results):
        print(f"{email}: {valid}")