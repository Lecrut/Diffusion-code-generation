import re

def validate_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

if __name__ == '__main__':
    sample_emails = [
        "user@example.com",
        "invalid.email",
        "test+tag@domain.co.uk",
        "bad@@domain.com"
    ]
    results = [validate_email(email) for email in sample_emails]
    for email, is_valid in zip(sample_emails, results):
        print(f"{email}: {is_valid}")