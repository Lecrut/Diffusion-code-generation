import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

if __name__ == '__main__':
    sample_emails = [
        "user@example.com",
        "invalid.email",
        "test.user@domain.co.uk",
        "@missing.local",
        "noatsign.com",
        "valid+tag@sub.domain.org",
        "spaces in@email.com"
    ]
    for email in sample_emails:
        result = validate_email(email)
        print(f"{email}: {result}")