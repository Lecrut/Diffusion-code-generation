import re

_DOMAIN_PATTERN = re.compile(r'^[a-zA-Z0-9]([a-zA-Z0-9-]*[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9-]*[a-zA-Z0-9])?)*\.[a-zA-Z]{2,}$')
_LOCAL_ALLOWED_CHARS = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&'*+-/=?^_`{|}~.")

def _is_valid_local_part(local: str) -> bool:
    if not local or len(local) > 64:
        return False
    if local.startswith('.') or local.endswith('.'):
        return False
    if '..' in local:
        return False
    for char in local:
        if char not in _LOCAL_ALLOWED_CHARS:
            return False
    return True

def _is_valid_domain_part(domain: str) -> bool:
    if not domain:
        return False
    return bool(_DOMAIN_PATTERN.match(domain))

def validate_email(address: str) -> bool:
    if not isinstance(address, str):
        return False
    parts = address.split('@')
    if len(parts) != 2:
        return False
    local, domain = parts
    return _is_valid_local_part(local) and _is_valid_domain_part(domain)

if __name__ == '__main__':
    test_cases = [
        "user.name@example.com",
        "invalid-email@",
        "@example.com",
        "user@@example.com",
        "user@sub.example.org",
        "bad..email@test.com",
        "user name@test.com",
        "user@test"
    ]
    for case in test_cases:
        result = validate_email(case)
        print(f"{case}: {result}")