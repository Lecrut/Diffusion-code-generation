import re

_domain_regex = re.compile(
    r'^(?!-)[A-Za-z0-9-]{1,63}(?<!-)(\.(?!-)[A-Za-z0-9-]{1,63}(?<!-))*\.[A-Za-z]{2,}$'
)

def validate_email(email):
    if not isinstance(email, str) or '@' not in email:
        return False

    local_part, domain_part = email.rsplit('@', 1)

    if not local_part or not domain_part:
        return False

    if not _domain_regex.match(domain_part):
        return False

    allowed_local_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._%+-")
    if not all(char in allowed_local_chars for char in local_part):
        return False

    if local_part.startswith('.') or local_part.endswith('.'):
        return False

    if '..' in local_part:
        return False

    return True

if __name__ == '__main__':
    test_cases = [
        "user@example.com",
        "invalid.email@",
        "@domain.com",
        "user@.com",
        "user@domain.c",
        "valid.email+tag@sub.domain.org",
        "user name@example.com",
        "",
        "a@b.co",
        ".user@example.com",
        "user.@example.com"
    ]
    for case in test_cases:
        print(validate_email(case))