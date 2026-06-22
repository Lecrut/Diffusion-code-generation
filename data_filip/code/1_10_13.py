def is_valid_email(email):
    if not isinstance(email, str):
        return False
    if not email or email[0] == '.' or email[-1] == '.':
        return False
    if '..' in email:
        return False
    if '@' not in email:
        return False
    parts = email.split('@')
    if len(parts) != 2:
        return False
    local, domain = parts
    if not local:
        return False
    if local[0] in '+-' or local[-1] in '+-':
        return False
    if local.count('.') == len(local):
        return False
    if len(local) > 64:
        return False
    if '.' not in domain:
        return False
    if domain[0] == '.' or domain[-1] == '.':
        return False
    if '..' in domain:
        return False
    if len(domain) > 255:
        return False
    domain_parts = domain.split('.')
    if any(len(part) > 63 for part in domain_parts):
        return False
    valid_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._%+-')
    for char in local:
        if char not in valid_chars:
            return False
    valid_domain_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-')
    for part in domain_parts:
        if not part:
            return False
        if part[0] == '-' or part[-1] == '-':
            return False
        for char in part:
            if char not in valid_domain_chars:
                return False
    return True

if __name__ == '__main__':
    test_cases = [
        "user@example.com",
        "user.name@domain.co.uk",
        "invalid@",
        "@invalid.com",
        "user@domain",
        "user..name@domain.com",
        "user@domain..com",
        "user+tag@example.org",
        "-user@example.com",
        "user@-domain.com",
        "a" * 64 + "@example.com",
        "user@" + "x" * 64 + ".com"
    ]
    for case in test_cases:
        print(case, is_valid_email(case))