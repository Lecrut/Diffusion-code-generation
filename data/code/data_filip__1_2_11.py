import re

_DOMAIN_REGEX = re.compile(
    r'^[a-zA-Z0-9]([a-zA-Z0-9\-]*[a-zA-Z0-9])?'
    r'(\.[a-zA-Z0-9]([a-zA-Z0-9\-]*[a-zA-Z0-9])?)*$'
)

_LOCAL_ALLOWED_CHARS = set(
    'abcdefghijklmnopqrstuvwxyz'
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    '0123456789'
    '._%+-'
)

def _is_valid_local(part: str) -> bool:
    if not part or len(part) > 64:
        return False
    if part.startswith('.') or part.endswith('.'):
        return False
    if '..' in part:
        return False
    for char in part:
        if char not in _LOCAL_ALLOWED_CHARS:
            return False
    return True

def _is_valid_domain(part: str) -> bool:
    if not part or len(part) > 253:
        return False
    if '.' not in part:
        return False
    if not _DOMAIN_REGEX.match(part):
        return False
    if part.endswith('.'):
        return False
    return True

def validate_email_address(email: str) -> bool:
    if not isinstance(email, str):
        return False
    if email.count('@') != 1:
        return False
    local, domain = email.split('@')
    return _is_valid_local(local) and _is_valid_domain(domain)

if __name__ == '__main__':
    test_cases = [
        "user.name@example.com",
        "bad@user@domain.com",
        ".startdot@example.com",
        "user@domain",
        "valid+tag@sub.domain.org",
        "123@456.789",
        "user..name@example.com"
    ]
    for case in test_cases:
        result = validate_email_address(case)
        print(f"{case}: {result}")