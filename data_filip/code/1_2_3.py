import re

DOMAIN_PATTERN = re.compile(r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

def validate_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    parts = email.split('@')
    if len(parts) != 2:
        return False
    local_part, domain_part = parts
    if not local_part:
        return False
    if '.' not in local_part and '_' not in local_part and '+' not in local_part and '-' not in local_part:
        if len(local_part) < 1 or len(local_part) > 64:
            return False
        if not local_part[0].isalnum() or not local_part[-1].isalnum():
            return False
    else:
        if not all(c.isalnum() or c in '._+-' for c in local_part):
            return False
        if local_part.startswith('.') or local_part.endswith('.') or '..' in local_part:
            return False
    if not domain_part:
        return False
    if not DOMAIN_PATTERN.match(domain_part):
        return False
    if '.' not in domain_part:
        return False
    return True

if __name__ == '__main__':
    test_emails = [
        "user@example.com",
        "invalid.email",
        "user@.com",
        "user@domain",
        "@example.com",
        "user@sub.domain.co.uk"
    ]
    for email in test_emails:
        print(validate_email(email))