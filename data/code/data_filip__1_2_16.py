import re

DOMAIN_REGEX = re.compile(r'^([a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$')

ALLOWED_LOCAL_CHARS = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.!#$%&\'*+/=?^_`{|}~-')

def validate_local_part(local):
    if not local:
        return False
    if len(local) > 64:
        return False
    for char in local:
        if char not in ALLOWED_LOCAL_CHARS:
            return False
    return True

def validate_domain_part(domain):
    if not domain:
        return False
    if len(domain) > 253:
        return False
    return bool(DOMAIN_REGEX.match(domain))

def is_valid_email(email):
    if not isinstance(email, str):
        return False
    if '@' not in email:
        return False
    parts = email.split('@')
    if len(parts) != 2:
        return False
    local, domain = parts
    if not validate_local_part(local):
        return False
    if not validate_domain_part(domain):
        return False
    return True

if __name__ == '__main__':
    samples = [
        "user@example.com",
        "invalid@.com",
        "user.name@domain.co.uk",
        "@domain.com",
        "user@domain",
        "a" * 65 + "@example.com",
        "user@-domain.com",
        "valid+tag@example.org",
        "user name@example.com",
        "user@exam ple.com"
    ]
    for sample in samples:
        result = is_valid_email(sample)
        print(result)