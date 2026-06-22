import re

domain_pattern = re.compile(r'^[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z]{2,}$')

def validate_email(email: str) -> bool:
    if not isinstance(email, str) or '@' not in email:
        return False
    parts = email.split('@')
    if len(parts) != 2:
        return False
    local_part, domain_part = parts
    if not local_part or '.' in local_part and local_part.startswith('.'):
        return False
    if local_part.startswith('.') or local_part.endswith('.'):
        return False
    if '..' in local_part:
        return False
    if not domain_pattern.match(domain_part):
        return False
    return True

if __name__ == '__main__':
    sample_emails = [
        "user@example.com",
        "invalid.email@com",
        "user@sub.domain.org",
        "bad@domain",
        "@missinglocal.com",
        "missing@.com",
        "valid.name@valid-domain.co.uk"
    ]
    for email in sample_emails:
        print(validate_email(email))