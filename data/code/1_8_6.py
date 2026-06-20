import re

def is_valid_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    if len(email) > 254:
        return False
    if email.count('@') != 1:
        return False
    local, domain = email.split('@')
    if not local or len(local) > 64:
        return False
    if not domain or len(domain) > 255:
        return False
    if domain.startswith('.') or domain.endswith('.'):
        return False
    if '..' in domain or '..' in local:
        return False
    local_pattern = r'^[a-zA-Z0-9!#$%&\'*+/=?^_`{|}~-]+(\.[a-zA-Z0-9!#$%&\'*+/=?^_`{|}~-]+)*$'
    domain_pattern = r'^(?!-)[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*$'
    if not re.match(local_pattern, local):
        return False
    if not re.match(domain_pattern, domain):
        return False
    domain_parts = domain.split('.')
    if len(domain_parts) < 2:
        return False
    if any(len(part) == 0 or len(part) > 63 for part in domain_parts):
        return False
    return True

if __name__ == '__main__':
    test_cases = [
        "user@example.com",
        "invalid.email@com",
        "user@sub.example.com",
        "user..name@example.com",
        "@example.com",
        "user@",
        "user@example",
        "very.(),:;<>[]\".VERY.\"very@\\ \"very\".strange@strange.com"
    ]
    for case in test_cases:
        print(is_valid_email(case))