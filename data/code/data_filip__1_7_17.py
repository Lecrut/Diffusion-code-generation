import re

def is_valid_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

if __name__ == '__main__':
    sample_emails = [
        "user@example.com",
        "invalid.email@",
        "test.user+tag@domain.co.uk",
        "@missing-local.com",
        "spaces in@email.com",
        "valid123@sub.domain.org"
    ]
    for email in sample_emails:
        print(f"{email}: {is_valid_email(email)}")