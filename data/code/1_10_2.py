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
    if len(local) > 64:
        return False
    if domain.endswith('.') or '..' in domain:
        return False
    if local.startswith('.') or local.endswith('.') or '..' in local:
        return False
    if any(c in local for c in '()<>[]:;@\\,'):
        return False
    if any(c in domain for c in '()<>[]:;@\\,'):
        return False
    if not all(c.isalnum() or c in '.-_' for c in local):
        return False
    if not all(c.isalnum() or c in '.-' for c in domain):
        return False
    parts = domain.split('.')
    if len(parts) < 2:
        return False
    for part in parts:
        if not part:
            return False
    return True

if __name__ == '__main__':
    test_cases = [
        "user@example.com",
        "invalid.email",
        "user@.com",
        "user@com.",
        "@example.com",
        "user@",
        "user name@example.com",
        "user@example",
        "valid.email+tag@sub.domain.co.uk",
        "",
        "a@b.c",
        "user@exam_ple.com",
        "user@exa-mple.com",
        "123@domain.org",
        "user@@domain.com",
        "user@domain..com"
    ]
    for case in test_cases:
        print(validate_email(case))