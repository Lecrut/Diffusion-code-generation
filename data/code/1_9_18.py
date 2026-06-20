import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

if __name__ == '__main__':
    test_emails = [
        "user@example.com",
        "invalid.email",
        "user@sub.domain.com",
        "user@.com",
        "@missing.com",
        "no_at_sign.com",
        "user@123.456.789"
    ]
    results = [validate_email(email) for email in test_emails]
    for email, is_valid in zip(test_emails, results):
        print(f"{email}: {is_valid}")