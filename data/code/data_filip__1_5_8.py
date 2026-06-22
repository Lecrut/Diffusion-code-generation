import re
import sys

def validate_email(email):
    if not isinstance(email, str):
        return False
    if len(email) > 254:
        return False
    pattern = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    if not pattern.match(email):
        return False
    if email.count('@') != 1:
        return False
    local, domain = email.split('@')
    if len(local) > 64:
        return False
    if not domain or len(domain) > 253:
        return False
    if domain.startswith('.') or domain.endswith('.'):
        return False
    if '..' in domain:
        return False
    if '..' in local:
        return False
    return True

if __name__ == '__main__':
    test_emails = [
        "user@example.com",
        "invalid.email@",
        "bad@domain",
        "valid.name+tag@sub.domain.co",
        "another@invalid",
        "toolong" + "a" * 70 + "@example.com"
    ]
    for email in test_emails:
        result = validate_email(email)
        print(f"{email}: {result}")