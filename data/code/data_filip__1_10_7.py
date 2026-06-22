import re

_EMAIL_REGEX = re.compile(
    r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"
)

def is_valid_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    if len(email) < 2 or len(email) > 254:
        return False
    if not _EMAIL_REGEX.match(email):
        return False
    local, domain = email.rsplit("@", 1)
    if not local:
        return False
    if not domain:
        return False
    if domain.count(".") < 1:
        return False
    for part in domain.split("."):
        if not part:
            return False
        if len(part) > 63:
            return False
    return True

if __name__ == '__main__':
    print(is_valid_email("user@example.com"))
    print(is_valid_email("invalid.email"))
    print(is_valid_email("@nodomain"))
    print(is_valid_email("user@.com"))
    print(is_valid_email("user@sub.domain.com"))