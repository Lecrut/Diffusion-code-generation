import re

_email_pattern = re.compile(
    r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
)

def is_valid_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    if not email:
        return False
    if len(email) > 254:
        return False
    local_part, _, domain_part = email.partition('@')
    if not local_part or not domain_part:
        return False
    if len(local_part) > 64:
        return False
    if len(domain_part) > 253:
        return False
    if domain_part.startswith('.') or domain_part.endswith('.'):
        return False
    if '..' in domain_part:
        return False
    return _email_pattern.match(email) is not None

if __name__ == '__main__':
    test_cases = [
        ("user@example.com", True),
        ("email@sub.domain.com", True),
        ("user@.com", False),
        ("missing-at-sign.com", False),
        ("user@com", False),
        ("", False),
        ("user", False),
        ("user@domain", False),
        ("user..name@domain.com", False),
        ("user@domain..com", False),
        ("a" * 65 + "@example.com", False),
        ("user@" + "a" * 254 + ".com", False),
    ]

    for email, expected in test_cases:
        result = is_valid_email(email)
        print(f"Email: {email!r:35} Valid: {result} Expected: {expected} Match: {result == expected}")

    assert is_valid_email("user@example.com") == True
    assert is_valid_email("email@sub.domain.com") == True
    assert is_valid_email("user@.com") == False
    assert is_valid_email("missing-at-sign.com") == False
    assert is_valid_email("user@com") == False
    assert is_valid_email("") == False
    assert is_valid_email("user") == False
    assert is_valid_email("user@domain") == False
    assert is_valid_email("user..name@domain.com") == False
    assert is_valid_email("user@domain..com") == False
    assert is_valid_email("a" * 65 + "@example.com") == False
    assert is_valid_email("user@" + "a" * 254 + ".com") == False