import re
import string

ALLOWED_LOCAL_CHARS = set(string.ascii_letters + string.digits + "!#$%&'*+/=?^_`{|}~-")
MAX_LOCAL_LENGTH = 64
MAX_DOMAIN_LENGTH = 253
MAX_EMAIL_LENGTH = 254

def _validate_local_part(local: str) -> bool:
    if not local:
        return False
    if len(local) > MAX_LOCAL_LENGTH:
        return False
    if local.startswith('.') or local.endswith('.'):
        return False
    if '..' in local:
        return False
    if '@' in local:
        return False
    for char in local:
        if char not in ALLOWED_LOCAL_CHARS:
            return False
    return True

def _validate_domain_part(domain: str) -> bool:
    if not domain:
        return False
    if len(domain) > MAX_DOMAIN_LENGTH:
        return False
    if domain.startswith('.') or domain.endswith('.'):
        return False
    if '..' in domain:
        return False
    if '@' in domain:
        return False
    labels = domain.split('.')
    if len(labels) < 2:
        return False
    for label in labels:
        if not label:
            return False
        if len(label) > 63:
            return False
        if label.startswith('-') or label.endswith('-'):
            return False
        if not label.isascii():
            return False
        for char in label:
            if char not in string.ascii_letters and char not in string.digits and char != '-':
                return False
    tld = labels[-1]
    if not tld.isalpha():
        return False
    return True

def is_valid_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    email = email.strip()
    if len(email) > MAX_EMAIL_LENGTH:
        return False
    if '@' not in email:
        return False
    if email.count('@') != 1:
        return False
    local, _, domain = email.partition('@')
    local_valid = _validate_local_part(local)
    if not local_valid:
        return False
    domain_valid = _validate_domain_part(domain)
    if not domain_valid:
        return False
    return True

if __name__ == '__main__':
    sample_emails = [
        "user@example.com",
        "invalid-email",
        "@example.com",
        "user@",
        "user..name@example.com",
        "user@example",
        "valid.user+tag@example.co.uk",
        "",
        "a@b.c",
        "user name@example.com",
        "123@123.123",
        "user@-example.com",
        "user@example-.com",
        "user@.example.com",
        "user@example..com",
        "very.long.local.part.that.exceeds.sixty.four.characters.limit@domain.com",
        "normal@example.com",
        "Abc@example.com",
        "user@sub.domain.example.com",
        "user@exam_ple.com",
        "user@192.168.1.1",
        "user@localhost",
        "user@com",
        "user@exa_mple.co",
        "user@exa..mple.com",
        "user@example.",
        ".user@example.com",
        "user.@example.com",
        "user@.example.com",
        "user@example.c-o-m",
        "user@example.c.m"
    ]
    for address in sample_emails:
        result = is_valid_email(address)
        print(f"{address}: {result}")