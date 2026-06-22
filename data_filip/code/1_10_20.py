def is_valid_email(email):
    if not isinstance(email, str):
        return False
    if not email:
        return False
    if email.count('@') != 1:
        return False
    local, domain = email.split('@')
    if not local or not domain:
        return False
    if local.startswith('.') or local.endswith('.'):
        return False
    if '..' in local:
        return False
    if domain.startswith('.') or domain.endswith('.'):
        return False
    if '..' in domain:
        return False
    if '@' in local or '@' in domain:
        return False
    if '.' not in domain:
        return False
    if domain[0] == '.' or domain[-1] == '.':
        return False
    domain_parts = domain.split('.')
    for part in domain_parts:
        if not part:
            return False
        if part[0] == '-' or part[-1] == '-':
            return False
    allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._-+")
    for char in local:
        if char not in allowed_chars:
            if char == '"':
                return False
            return False
    for char in domain:
        if char not in allowed_chars and char != '.':
            return False
    return True

if __name__ == '__main__':
    test_cases = [
        "user@example.com",
        "user.name+tag@sub.domain.co",
        "invalid@.com",
        "invalid@example",
        "@example.com",
        "user@",
        "user..name@example.com",
        "user@exam ple.com",
        "user@-example.com",
        "user@example-.com",
        "user@example.c",
        "valid_user+tag-1@sub.domain.org"
    ]
    results = []
    for case in test_cases:
        results.append(is_valid_email(case))
    print(results)