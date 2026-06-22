import re

def validate_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

if __name__ == '__main__':
    sample_emails = ["user@example.com", "invalid.email", "test+tag@domain.org", "no-at-sign.com", "another@sub.domain.com"]
    results = {email: validate_email(email) for email in sample_emails}
    print(results)