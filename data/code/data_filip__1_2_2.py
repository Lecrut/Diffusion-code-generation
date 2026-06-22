import re

_email_domain_pattern = re.compile(r'^[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?)*\.[a-zA-Z]{2,}$')

def validate_email(email: str) -> bool:
    if '@' not in email:
        return False
    parts = email.split('@')
    if len(parts) != 2:
        return False
    local_part, domain_part = parts
    if not local_part or not domain_part:
        return False
    if len(local_part) > 64:
        return False
    if '..' in local_part:
        return False
    for char in local_part:
        if not (char.isalnum() or char in '.!#$%&\'*+/-=?^_`{|}~'):
            return False
    if _email_domain_pattern.match(domain_part):
        return True
    return False

if __name__ == '__main__':
    test_emails = [
        "user@example.com",
        "invalid-email.com",
        "user@@example.com",
        "user@-invalid.com",
        ".user@example.com",
        "user@.example.com"
    ]
    for email in test_emails:
        print(validate_email(email))