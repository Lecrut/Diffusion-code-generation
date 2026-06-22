import re

DOMAIN_REGEX = re.compile(r'^[a-zA-Z0-9](?:[a-zA-Z0-9\-]*[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9\-]*[a-zA-Z0-9])?)*\.[a-zA-Z]{2,}$')

def validate_email(email):
    if not isinstance(email, str):
        return False
    parts = email.split('@')
    if len(parts) != 2:
        return False
    local_part, domain_part = parts
    if not local_part or not domain_part:
        return False
    allowed_local_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._%+-')
    if not all(c in allowed_local_chars for c in local_part):
        return False
    if local_part[0] in '._%+-' or local_part[-1] in '._%+-':
        return False
    if '..' in local_part:
        return False
    if not DOMAIN_REGEX.match(domain_part):
        return False
    return True

if __name__ == '__main__':
    sample_emails = [
        "user@example.com",
        "invalid.email@",
        "@example.com",
        "user@.com",
        "user@com",
        "user name@example.com",
        "valid.email+tag@sub.domain.org",
        "a@b.cc",
        "user@-example.com",
        "user@example-.com",
        "",
        12345,
        "user@example.com.",
        "user..name@example.com"
    ]
    for email in sample_emails:
        result = validate_email(email)
        print(result)