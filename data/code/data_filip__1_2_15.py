import re

DOMAIN_REGEX = re.compile(r'^[a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)*$')

def validate_email(email):
    if not isinstance(email, str) or '@' not in email:
        return False

    parts = email.split('@')
    if len(parts) != 2:
        return False

    local_part, domain_part = parts

    if not local_part or not domain_part:
        return False

    if local_part.count('.') > 0 and (local_part.startswith('.') or local_part.endswith('.')):
        return False

    for i in range(len(local_part) - 1):
        if local_part[i] == '.' and local_part[i + 1] == '.':
            return False

    if not DOMAIN_REGEX.match(domain_part):
        return False

    return True

if __name__ == '__main__':
    print(validate_email('user@example.com'))
    print(validate_email('invalid.email'))
    print(validate_email('@domain.com'))
    print(validate_email('user@'))
    print(validate_email('user.name@sub.domain.org'))
    print(validate_email('user..name@domain.com'))
    print(validate_email('user@.com'))
    print(validate_email('user@domain.c'))