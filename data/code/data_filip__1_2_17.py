import re

DOMAIN_REGEX = re.compile(r'^([a-zA-Z0-9]([a-zA-Z0-9\-]*[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$')

ALLOWED_LOCAL_CHARS = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.!#$%&'*+/=?^_`{|}~-")

def check_local_part(local):
    if not local:
        return False
    if len(local) > 64:
        return False
    for char in local:
        if char not in ALLOWED_LOCAL_CHARS:
            return False
    if '..' in local:
        return False
    if local.startswith('.') or local.endswith('.'):
        return False
    return True

def check_domain_part(domain):
    if not domain:
        return False
    if len(domain) > 253:
        return False
    return bool(DOMAIN_REGEX.match(domain))

def is_valid_email(address):
    if not isinstance(address, str):
        return False
    if address.count('@') != 1:
        return False
    local, domain = address.split('@')
    if not check_local_part(local):
        return False
    if not check_domain_part(domain):
        return False
    return True

if __name__ == '__main__':
    samples = [
        "user@example.com",
        "invalid.email",
        "user@.com",
        "@domain.com",
        "user@domain",
        "user..name@example.com",
        "a@b.co",
        "very.common@example.org",
        "disposable.style.email.with+symbol@example.com",
        "other.email-with-hyphen@example.com",
        "fully-qualified-domain@example.com",
        "x@example.com",
        "example-indeed@strange-example.com",
        "user.name+tag+sorting@example.com",
        "1234567890@example.com",
        "email@example.museum",
        "user@localhost",
        "user@192.168.1.1"
    ]
    for sample in samples:
        print(is_valid_email(sample))