import re

def validate_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    max_length = 254
    if len(email) > max_length:
        return False
    local_part, _, domain_part = email.rpartition('@')
    if not local_part or not domain_part:
        return False
    if len(local_part) > 64:
        return False
    if len(domain_part) > 253:
        return False
    domain_regex = re.compile(
        r'^(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$'
    )
    if not domain_regex.match(domain_part):
        return False
    local_regex = re.compile(
        r'^(?:[a-zA-Z0-9!#$%&\'*+/=?^_`{|}~-]|(?:\\[^\s]))*$'
    )
    if not local_regex.match(local_part):
        return False
    if '..' in local_part or local_part.startswith('.') or local_part.endswith('.'):
        return False
    return True

if __name__ == '__main__':
    print(validate_email("user@example.com"))
    print(validate_email("invalid-email"))
    print(validate_email("@missing-local.com"))
    print(validate_email("user@.com"))
    print(validate_email("user@-invalid.com"))
    print(validate_email("user name@example.com"))