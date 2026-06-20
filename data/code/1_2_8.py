import re

_DOMAIN_RE = re.compile(r'^([a-zA-Z0-9]([a-zA-Z0-9\-]*[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$')

def validate_email(email):
    if not isinstance(email, str) or '@' not in email:
        return False
    parts = email.split('@')
    if len(parts) != 2:
        return False
    local_part, domain_part = parts
    if not local_part or not domain_part:
        return False
    if not all(c.isalnum() or c in '.-_+' for c in local_part):
        return False
    if local_part.startswith('.') or local_part.endswith('.') or '..' in local_part:
        return False
    return bool(_DOMAIN_RE.match(domain_part))

if __name__ == '__main__':
    print(validate_email("user@example.com"))
    print(validate_email("invalid-email@"))
    print(validate_email("@domain.com"))
    print(validate_email("user@.com"))
    print(validate_email("user@domain"))
    print(validate_email("user.name@sub.domain.org"))
    print(validate_email("bad..email@example.com"))