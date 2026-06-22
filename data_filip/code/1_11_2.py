import re

def validate_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

if __name__ == '__main__':
    sample_emails = [
        "user@example.com",
        "invalid-email@.com",
        "another@valid.example.org",
        "@missing-local.com",
        "no-at-sign.com",
        "user@sub.domain.co.uk",
        "bad user @example.com",
        "valid123@test-domain.com"
    ]
    for email in sample_emails:
        print(validate_email(email))