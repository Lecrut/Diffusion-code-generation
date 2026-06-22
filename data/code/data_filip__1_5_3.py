import re
import sys

def validate_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    if len(email) > 254:
        return False
    try:
        email.encode('ascii').decode('ascii')
    except UnicodeDecodeError:
        return False
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        return False
    parts = email.split('@')
    if len(parts) != 2:
        return False
    local, domain = parts
    if not local or local.startswith('.') or local.endswith('.'):
        return False
    if '..' in local:
        return False
    if not domain or '.' not in domain:
        return False
    if domain.startswith('-') or domain.endswith('-'):
        return False
    if domain.startswith('.') or domain.endswith('.'):
        return False
    if '..' in domain:
        return False
    return True

if __name__ == '__main__':
    sample_emails = [
        "user@example.com",
        "test.email+tag@domain.co.uk",
        "invalid.email@",
        "@missing.local.com",
        "no-at-sign.com",
        "spaces in email@test.com",
        "valid_user123@sub.domain.org"
    ]
    for email in sample_emails:
        result = validate_email(email)
        print(f"{email}: {result}")