import re

ALLOWED_LOCAL_CHARS = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._%+-")
DOMAIN_REGEX = re.compile(r"^([a-zA-Z0-9]([a-zA-Z0-9\-]*[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$")

def _is_valid_local_part(local_part):
    if not local_part:
        return False
    if len(local_part) > 64:
        return False
    if local_part.startswith(".") or local_part.endswith(".") or ".." in local_part:
        return False
    for char in local_part:
        if char not in ALLOWED_LOCAL_CHARS:
            return False
    return True

def _is_valid_domain_part(domain_part):
    if not domain_part:
        return False
    if len(domain_part) > 253:
        return False
    return bool(DOMAIN_REGEX.match(domain_part))

def validate_email_address(email):
    if not isinstance(email, str):
        return False
    if email.count("@") != 1:
        return False
    local_part, domain_part = email.split("@")
    return _is_valid_local_part(local_part) and _is_valid_domain_part(domain_part)

if __name__ == "__main__":
    print(validate_email_address("user@example.com"))
    print(validate_email_address("bad@domain"))
    print(validate_email_address("@missing.com"))
    print(validate_email_address("missing@.com"))
    print(validate_email_address("valid.name+tag@sub.domain.co.uk"))
    print(validate_email_address("too..many..dots@domain.com"))
    print(validate_email_address("starts.dot@domain.com"))