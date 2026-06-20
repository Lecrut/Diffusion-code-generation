def validate_email(email):
    if not isinstance(email, str) or '@' not in email:
        return False
    local, domain = email.rsplit('@', 1)
    if not local or not domain:
        return False
    if len(domain) > 253 or len(local) > 64:
        return False
    parts = domain.split('.')
    if len(parts) < 2:
        return False
    for part in parts:
        if not part:
            return False
        if len(part) > 63:
            return False
        if part.startswith('-') or part.endswith('-'):
            return False
        if not all(c.isalnum() or c == '-' for c in part):
            return False
    if parts[-1].isalpha() is False:
        return False
    allowed_specials = set('.!#$%&\'*+/=?^_`{|}~')
    if email.startswith('.') or email.endswith('.'):
        return False
    if '..' in email.split('@')[0]:
        return False
    for char in local:
        if not (char.isalnum() or char in allowed_specials):
            return False
    return True

if __name__ == '__main__':
    test_cases = [
        "user@example.com",
        "invalid.email",
        "@missing-local.com",
        "no-at-sign.com",
        "user@.com",
        "user@com.",
        "user@exam ple.com",
        "user.name+tag@domain.co.uk",
        "a@b.cd",
        "",
        "user@-domain.com",
        "user@domain-.com",
        ".user@example.com",
        "user.@example.com",
        "user..name@example.com",
        "user@example.c",
        "very.long.local.part.that.exceeds.sixtyfour.characters.limit.which.is.not.allowed.by.rfc@example.com",
    ]
    results = {email: validate_email(email) for email in test_cases}
    for email, valid in results.items():
        print(f"{repr(email)}: {valid}")