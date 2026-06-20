import re

def validate_email_syntax(email):
    if not isinstance(email, str):
        return False
    if len(email) > 254:
        return False
    parts = email.split("@")
    if len(parts) != 2:
        return False
    user, domain = parts
    if not user or len(user) > 64:
        return False
    if not domain or len(domain) > 255:
        return False
    if "." not in domain:
        return False
    if domain.startswith(".") or domain.endswith("."):
        return False
    if ".." in domain:
        return False
    if user.startswith(".") or user.endswith("."):
        return False
    if ".." in user:
        return False
    pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    return bool(pattern.match(email))

if __name__ == '__main__':
    test_cases = [
        "user@example.com",
        "invalid.email",
        "user@.com",
        "user@domain.co.uk",
        "@domain.com",
        "user@domain",
        "user..name@domain.com",
        "user.name@domain..com"
    ]
    for test in test_cases:
        result = validate_email_syntax(test)
        print(result)