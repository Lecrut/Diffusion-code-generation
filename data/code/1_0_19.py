import re

EMAIL_REGEX = re.compile(
    r'^(?P<local>[a-zA-Z0-9._%+-]+)@'
    r'(?P<domain>[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$'
)

def check_local_part(local: str) -> bool:
    if not local or local.startswith('.') or local.endswith('.') or '..' in local:
        return False
    return True

def check_domain_part(domain: str) -> bool:
    if not domain:
        return False
    parts = domain.split('.')
    if len(parts) < 2:
        return False
    for part in parts:
        if not part or part.startswith('-') or part.endswith('-'):
            return False
    return True

def validate_email_address(address: str) -> bool:
    if not isinstance(address, str):
        return False
    match = EMAIL_REGEX.match(address)
    if not match:
        return False
    local = match.group('local')
    domain = match.group('domain')
    return check_local_part(local) and check_domain_part(domain)

if __name__ == '__main__':
    test_cases = [
        "alice@example.com",
        "bob.smith@sub.domain.co.uk",
        "charlie..dane@test.com",
        "dave@invaliddomain",
        ".startdot@bad.com",
        "valid_name+tag@valid-site.org",
        "bad@.com",
        "user@domain",
        "spaces@domain.com",
        "last.dot.@domain.com"
    ]
    output = [validate_email_address(email) for email in test_cases]
    print(output)