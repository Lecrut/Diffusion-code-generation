def validate_email(email):
    if not isinstance(email, str):
        return False
    if not email or email[0] == '.' or email[-1] == '.':
        return False
    if email.count('@') != 1:
        return False
    local, domain = email.split('@')
    if not local or not domain or domain[0] == '.' or domain[-1] == '.':
        return False
    if '..' in local or '..' in domain:
        return False
    if '.' not in domain:
        return False
    domain_parts = domain.split('.')
    for part in domain_parts:
        if not part or part[0] == '-' or part[-1] == '-':
            return False
    allowed_local = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&'*+/=?^_`{|}~-")
    for char in local:
        if char not in allowed_local:
            if char not in '._+':
                return False
    allowed_domain = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-")
    for char in domain:
        if char not in allowed_domain:
            return False
    return True

if __name__ == '__main__':
    test_cases = [
        ("user@example.com", True),
        ("user.name+tag@sub.domain.org", True),
        ("invalid.email", False),
        ("@example.com", False),
        ("user@", False),
        ("user@.com", False),
        ("user@example", False),
        ("user..name@example.com", False),
        ("user@exam--ple.com", True),
        ("user@-example.com", False),
    ]
    results = []
    for email, expected in test_cases:
        result = validate_email(email)
        assert result == expected, f"Failed for {email}: expected {expected}, got {result}"
        results.append((email, result))
    for email, result in results:
        print(f"{email}: {result}")