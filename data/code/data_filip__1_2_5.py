import re

DOMAIN_PATTERN = re.compile(r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

def is_valid_email(email: str) -> bool:
    if not isinstance(email, str) or '@' not in email:
        return False
    
    parts = email.split('@')
    if len(parts) != 2:
        return False
    
    local_part, domain_part = parts
    
    if not local_part or not domain_part:
        return False
    
    if '.' not in domain_part:
        return False
    
    if not DOMAIN_PATTERN.match(domain_part):
        return False
    
    for char in local_part:
        if not (char.isalnum() or char in '.-_+'):
            return False
    
    if local_part.startswith('.') or local_part.endswith('.'):
        return False
    
    return True

if __name__ == '__main__':
    test_cases = [
        "user@example.com",
        "invalid.email@domain",
        "@missing-local.com",
        "no-at-sign.com",
        "user@.com",
        "user@domain.c",
        "valid_user+tag@sub.domain.org"
    ]
    
    for test_email in test_cases:
        result = is_valid_email(test_email)
        print(f"{test_email}: {result}")