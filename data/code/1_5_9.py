import re
from typing import List, Tuple

_LOCAL_PART_PATTERN = re.compile(r'^[a-zA-Z0-9_.+-]+$', re.ASCII)
_DOMAIN_PART_PATTERN = re.compile(r'^[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*$', re.ASCII)
_MAX_EMAIL_LENGTH = 254
_MAX_LOCAL_LENGTH = 64

def _is_valid_local(local: str) -> bool:
    if not local or len(local) > _MAX_LOCAL_LENGTH:
        return False
    return bool(_LOCAL_PART_PATTERN.match(local))

def _is_valid_domain(domain: str) -> bool:
    if not domain:
        return False
    if len(domain) > 253:
        return False
    if domain.startswith('-') or domain.endswith('-'):
        return False
    if '..' in domain:
        return False
    if domain[0] == '.' or domain[-1] == '.':
        return False
    return bool(_DOMAIN_PART_PATTERN.match(domain))

def validate_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    if len(email) > _MAX_EMAIL_LENGTH:
        return False
    if email.count('@') != 1:
        return False
    try:
        local, domain = email.split('@')
        return _is_valid_local(local) and _is_valid_domain(domain)
    except ValueError:
        return False

def run_validation_batch(emails: List[str]) -> List[Tuple[str, bool]]:
    return [(email, validate_email(email)) for email in emails]

if __name__ == '__main__':
    test_data = [
        "user@example.com",
        "invalid.email@",
        "another@invalid",
        "test.user+tag@sub.domain.co",
        "spaces in@email.com",
        "@missinglocal.com",
        "valid123@sub.domain.org",
        "-start@domain.com",
        "end.@domain.com",
        "double..dot@domain.com",
        "a" * 65 + "@domain.com",
        "user@" + "x" * 254,
        None,
        12345
    ]
    results = run_validation_batch(test_data)
    for email, is_valid in results:
        print(email, is_valid)