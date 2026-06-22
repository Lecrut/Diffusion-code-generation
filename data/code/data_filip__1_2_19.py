import re
import string

_DOMAIN_PATTERN = re.compile(r'^[a-zA-Z0-9]([a-zA-Z0-9-]*[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9-]*[a-zA-Z0-9])?)*\.[a-zA-Z]{2,}$')
_ALLOWED_LOCAL_CHARS = frozenset(string.ascii_letters + string.digits + '._%+-')

def _is_valid_local_part(part: str) -> bool:
    if not part:
        return False
    if len(part) > 64:
        return False
    if part.startswith('.') or part.endswith('.'):
        return False
    if '..' in part:
        return False
    for char in part:
        if char not in _ALLOWED_LOCAL_CHARS:
            return False
    return True

def _is_valid_domain_part(part: str) -> bool:
    if not part:
        return False
    if len(part) > 253:
        return False
    if part.startswith('-') or part.endswith('-'):
        return False
    return bool(_DOMAIN_PATTERN.match(part))

def validate_email_address(address: str) -> bool:
    if not isinstance(address, str):
        return False
    if address.count('@') != 1:
        return False
    local_part, domain_part = address.split('@')
    if not _is_valid_local_part(local_part):
        return False
    if not _is_valid_domain_part(domain_part):
        return False
    return True

if __name__ == '__main__':
    test_cases = [
        "user@example.com",
        "invalid.email@",
        "user@.com",
        "..user@example.com",
        "user.name+tag@sub.domain.co.uk",
        "a-b@c-d.org"
    ]
    for test in test_cases:
        result = validate_email_address(test)
        print(result)