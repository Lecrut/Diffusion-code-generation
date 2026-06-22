import re

_VALID_EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

def validate_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    if len(email) > 254:
        return False
    local, sep, domain = email.rpartition('@')
    if not sep:
        return False
    if not local or not domain:
        return False
    if len(local) > 64:
        return False
    if len(domain) > 253:
        return False
    if domain.startswith('-') or domain.endswith('-'):
        return False
    if '..' in local or '..' in domain:
        return False
    return bool(_VALID_EMAIL_REGEX.match(email))

if __name__ == '__main__':
    test_emails = [
        ("user@example.com", True),
        ("invalid@", False),
        ("@example.com", False),
        ("a@b.c", True),
        ("test.email+tag@domain.co.uk", True),
        ("no_at_sign", False),
        ("user@-invalid.com", False),
        ("user@valid.com-", False),
        (123, False),
        ("", False),
    ]
    
    for email, expected in test_emails:
        result = validate_email(email)
        assert result == expected, f"Failed for {email}: expected {expected}, got {result}"
        print(f"{email}: {result}")