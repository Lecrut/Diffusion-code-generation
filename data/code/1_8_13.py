import re

email_pattern = re.compile(
    r'^(?:[a-zA-Z0-9!#$%&\'*+/=?^_`{|}~-]+'
    r'(?:\.[a-zA-Z0-9!#$%&\'*+/=?^_`{|}~-]+)*'
    r'|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]'
    r'|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")'
    r'@'
    r'(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+'
    r'[a-zA-Z]{2,}$',
    re.ASCII
)

def is_valid_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    if not email or len(email) > 320:
        return False
    if email.count('@') != 1:
        return False
    local_part, domain_part = email.split('@')
    if not local_part or len(local_part) > 64:
        return False
    if not domain_part or len(domain_part) > 253:
        return False
    if domain_part.startswith('.') or domain_part.endswith('.'):
        return False
    return bool(email_pattern.match(email))

if __name__ == '__main__':
    test_cases = [
        "user@example.com",
        "user.name+tag@sub.example.co.uk",
        "invalid-email@",
        "@missing-local.com",
        "user@invalid",
        "spaces @ example.com",
        '"quoted"@example.com',
        "valid-123@test.org"
    ]
    
    for test_email in test_cases:
        print(is_valid_email(test_email))