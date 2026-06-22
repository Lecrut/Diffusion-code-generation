import re

def is_valid_email(email):
    if not isinstance(email, str):
        return False
    if len(email) > 320:
        return False
    if email.startswith('.') or email.endswith('.'):
        return False
    if '..' in email:
        return False
    pattern = re.compile(
        r"^(?P<local>[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]"
        r"(?:[a-zA-Z0-9!#$%&'*+/=?^_`{|}~.-]*)"
        r"@"
        r"(?P<domain>"
        r"(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+"
        r"[a-zA-Z]{2,})"
        r"$"
    )
    if not pattern.match(email):
        return False
    parts = email.split('@')
    if len(parts) != 2:
        return False
    local_part = parts[0]
    domain_part = parts[1]
    if local_part.startswith('"') and local_part.endswith('"'):
        if len(local_part) < 2:
            return False
        inner = local_part[1:-1]
        if '..' in inner or inner.startswith('.') or inner.endswith('.'):
            return False
        return True
    if local_part.startswith('.') or local_part.endswith('.'):
        return False
    if len(domain_part) == 0:
        return False
    if domain_part.startswith('-') or domain_part.endswith('-'):
        return False
    if '..' in domain_part:
        return False
    for segment in domain_part.split('.'):
        if len(segment) == 0:
            return False
        if segment.startswith('-') or segment.endswith('-'):
            return False
        if not re.match(r'^[a-zA-Z0-9-]+$', segment):
            return False
    return True

if __name__ == '__main__':
    test_emails = [
        "simple@example.com",
        "very.common@example.com",
        "disposable.style.email.with+symbol@example.com",
        "other.email-with-hyphen@example.com",
        "fully-qualified-domain@example.com",
        "user.name+tag+sorting@example.com",
        "x@example.com",
        "example-indeed@strange-example.com",
        "example@s.example",
        "email@example.co.uk",
        "postmaster@localhost",
        "Abc.example.com",
        "A@b@c@example.com",
        "a(b)c,d:e;f@g",
        "JoeSmith@example.com",
        "email..email@example.com",
        "email@example@domain.com",
        "@example.com",
        "email@example",
        "email@-example.com",
        "email@example..com",
        ".email@example.com",
        "email.@example.com",
        "email@example.com.",
        "email@example.co",
        "very.(),:;<>[]\".VERY.\"very@\\ \"very\".unusual@strange.example.com"
    ]
    for addr in test_emails:
        print(f"{addr}: {is_valid_email(addr)}")