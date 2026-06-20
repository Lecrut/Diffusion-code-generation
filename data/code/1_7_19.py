import re

_PATTERN = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

def validate_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    if len(email) > 254:
        return False
    local, domain = email.rsplit('@', 1)
    if not local or not domain:
        return False
    if local.startswith('.') or local.endswith('.') or '..' in local:
        return False
    if domain.startswith('-') or domain.endswith('-'):
        return False
    if not _PATTERN.match(email):
        return False
    return True

if __name__ == '__main__':
    print(validate_email("user@example.com"))
    print(validate_email("invalid-email"))
    print(validate_email("user@sub.domain.com"))
    print(validate_email("@missing.com"))
    print(validate_email("user@.com"))