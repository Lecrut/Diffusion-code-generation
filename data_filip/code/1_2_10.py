import re

DOMAIN_REGEX = re.compile(r'^[a-zA-Z0-9]([a-zA-Z0-9\-]*[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9\-]*[a-zA-Z0-9])?)*$')

def validate_email(email):
    if not isinstance(email, str):
        return False
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
    if len(domain_part) > 253:
        return False
    allowed_local_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.!#$%&\'*+/=?^_`{|}~-')
    if not all(c in allowed_local_chars for c in local_part):
        return False
    if local_part[0] == '.' or local_part[-1] == '.':
        return False
    if '..' in local_part:
        return False
    if not DOMAIN_REGEX.match(domain_part):
        return False
    if domain_part[0] == '.' or domain_part[-1] == '.':
        return False
    return True

if __name__ == '__main__':
    samples = [
        "user@example.com",
        "invalid@",
        "@domain.com",
        "user@.com",
        "user@domain.",
        "user name@domain.com",
        "user@domain..com",
        "a@b.c",
        "test+tag@sub.domain.co.uk",
        "",
        "simple@example.com",
        "very.common@example.org",
        "disposable.style.email.with+symbol@example.com",
        "other.email-with-hyphen@example.com",
        "fully-qualified-domain@example.com",
        "user.name+tag+sorting@example.com",
        "x@example.com",
        "example-indeed@strange-example.com",
        "test/test@test.com",
        "not-an-email",
        "user@domain",
    ]
    for sample in samples:
        result = validate_email(sample)
        print(result)