import re

INVALID_CHARS_PATTERN = re.compile(r'[^\w\.\+\-@]')
LOCAL_PART_PATTERN = re.compile(r'^[a-zA-Z0-9_+\-.]+(?:\.[a-zA-Z0-9_+\-.]+)*$')
DOMAIN_PATTERN = re.compile(r'^[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$')

def is_valid_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    if not email or email.startswith('.') or email.endswith('.'):
        return False
    if '..' in email:
        return False
    if '@' not in email:
        return False
    parts = email.split('@')
    if len(parts) != 2:
        return False
    local, domain = parts
    if not local or len(local) > 64:
        return False
    if not domain or len(domain) > 255:
        return False
    if domain.startswith('.') or domain.endswith('.'):
        return False
    if domain.startswith('-') or domain.endswith('-'):
        return False
    if any(part.startswith('-') or part.endswith('-') for part in domain.split('.')):
        return False
    if len(local) == 0 or local[0] == '.' or local[-1] == '.':
        return False
    if INVALID_CHARS_PATTERN.search(local):
        return False
    if not LOCAL_PART_PATTERN.match(local):
        return False
    if INVALID_CHARS_PATTERN.search(domain):
        return False
    if not DOMAIN_PATTERN.match(domain):
        return False
    domain_parts = domain.split('.')
    if len(domain_parts) < 2:
        return False
    for part in domain_parts:
        if len(part) == 0 or len(part) > 63:
            return False
    return True

if __name__ == '__main__':
    test_emails = [
        "user@example.com",
        "user.name+tag@sub.domain.org",
        "invalid-email@",
        "@invalid.com",
        "user@.com",
        "user@example..com",
        "user@-example.com",
        "user@exam_ple.com",
        "",
        "user name@example.com",
        "user@exam ple.com",
        ".user@example.com",
        "user.@example.com",
        "user..name@example.com",
        "a@b.co",
        "very.long.email.address.with.many.dots@example.org"
    ]
    for email in test_emails:
        print(f"{email}: {is_valid_email(email)}")