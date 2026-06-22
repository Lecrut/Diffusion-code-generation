import re

DOMAIN_REGEX = re.compile(r'^[a-zA-Z0-9]([a-zA-Z0-9-]*[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9-]*[a-zA-Z0-9])?)*$')
LOCAL_ALLOWED_CHARS = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._%+-")

def _is_valid_local_part(local: str) -> bool:
    if not local or len(local) > 64:
        return False
    if local.startswith('.') or local.endswith('.'):
        return False
    if '..' in local:
        return False
    for char in local:
        if char not in LOCAL_ALLOWED_CHARS:
            return False
    return True

def _is_valid_domain_part(domain: str) -> bool:
    if not domain:
        return False
    if len(domain) > 253:
        return False
    return bool(DOMAIN_REGEX.match(domain))

def validate_email_address(email: str) -> bool:
    if not isinstance(email, str):
        return False
    if email.count('@') != 1:
        return False
    local_part, domain_part = email.split('@')
    if not _is_valid_local_part(local_part):
        return False
    if not _is_valid_domain_part(domain_part):
        return False
    return True

if __name__ == '__main__':
    test_cases = [
        "user.name+tag@example.com",
        "invalid.email@invalid",
        "bad..double@domain.com",
        "valid_user123@sub.domain.org",
        "no_at_sign",
        "@nodomain.com",
        "nolocal@"
    ]
    for case in test_cases:
        result = validate_email_address(case)
        print(f"{case}: {result}")