def validate_email(email):
    if not isinstance(email, str):
        return False
    if len(email) < 5 or len(email) > 254:
        return False
    if '@' not in email:
        return False
    local, domain = email.rsplit('@', 1)
    if not local or not domain:
        return False
    if '.' not in domain:
        return False
    domain_parts = domain.split('.')
    for part in domain_parts:
        if not part:
            return False
        if not all(c.isalnum() or c == '-' for c in part):
            return False
        if part.startswith('-') or part.endswith('-'):
            return False
    if not all(c.isalnum() or c in '.!#$%&\'*+/=?^_`{|}~-' for c in local):
        return False
    if local.startswith('.') or local.endswith('.'):
        return False
    return True

if __name__ == '__main__':
    samples = [
        'user@example.com',
        'invalid.',
        'user@.com',
        'user@com',
        '',
        'user@domain.co.uk',
        'user.name@domain.com',
        '@domain.com',
        'user@',
        'user name@domain.com',
        'user@domain..com',
        'u@b.c'
    ]
    for s in samples:
        print(validate_email(s))