import re
import string

_email_regex = re.compile(
    r'^(?P<local>[a-zA-Z0-9_.+-]+)'
    r'@'
    r'(?P<domain>[a-zA-Z0-9-]+)'
    r'(\.(?P=domain)*|'
    r'[a-zA-Z]{2,})$'
)

def is_valid_email(email):
    if not isinstance(email, str):
        return False
    if not email or len(email) > 254:
        return False
    if email.startswith('.') or email.endswith('.'):
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
    if not domain:
        return False
    if domain.startswith('.') or domain.endswith('.'):
        return False
    if '..' in domain:
        return False
    if len(domain) > 255:
        return False
    domain_parts = domain.split('.')
    if any(len(part) > 63 for part in domain_parts):
        return False
    if any(not part.isascii() or not all(c in string.ascii_letters + string.digits + '-' for c in part) for part in domain_parts):
        return False
    if any(c not in string.ascii_letters + string.digits + '_-+.' for c in local):
        return False
    if local.startswith('-') or local.endswith('-'):
        return False
    if local.startswith('_') or local.endswith('_'):
        return False
    if '.' in local and local.startswith('.'):
        return False
    return True

if __name__ == '__main__':
    test_cases = [
        ("user@example.com", True),
        ("user.name@sub.domain.com", True),
        ("invalid-email@", False),
        ("@domain.com", False),
        ("user@domain", True),
        ("user@domain.c", False),
        ("user..name@example.com", False),
        ("user@domain..com", False),
        ("user@example.com.", False),
        (".user@example.com", False),
        ("user@example.co.uk", True),
        ("user_name+tag@example.org", True),
        ("user@-domain.com", False),
        ("user@domain-.com", False),
        ("", False),
        ("a", False),
        ("a@b", True),
        ("user name@example.com", False),
    ]
    for email, expected in test_cases:
        result = is_valid_email(email)
        assert result == expected, f"Failed for {email}: expected {expected}, got {result}"
        print(f"{email}: {result}")