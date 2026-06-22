import re

_EMAIL_REGEX = re.compile(
    r'^[a-zA-Z0-9.!#$%&\'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$'
)

def is_valid_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    if len(email) > 254:
        return False
    if len(email) == 0:
        return False
    if email.startswith('.') or email.endswith('.'):
        return False
    if '@' in email:
        local_part, _, domain_part = email.rpartition('@')
        if len(local_part) == 0 or len(domain_part) == 0:
            return False
        if '..' in local_part or '..' in domain_part:
            return False
        if domain_part.startswith('-') or domain_part.endswith('-'):
            return False
    return bool(_EMAIL_REGEX.match(email))

if __name__ == '__main__':
    test_emails = [
        "user@example.com",
        "invalid.email",
        "another@domain.org",
        "no-at-sign.com",
        "@missing-local.com",
        "spaces in@email.com",
        "valid+tag@sub.domain.co.uk",
        "",
        "a" * 64 + "@example.com",
        "user@"
    ]
    
    for email in test_emails:
        result = is_valid_email(email)
        print(f"Email: {email!r} -> Valid: {result}")