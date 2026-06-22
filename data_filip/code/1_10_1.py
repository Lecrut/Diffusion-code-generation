import re

_VALID_EMAIL_RE = re.compile(
    r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
)

def is_valid_email(email):
    if not isinstance(email, str):
        return False
    return bool(_VALID_EMAIL_RE.match(email))

if __name__ == '__main__':
    print(is_valid_email("user@example.com"))
    print(is_valid_email("invalid-email"))
    print(is_valid_email("another.test+tag@domain.co.uk"))
    print(is_valid_email("missing-at-sign.com"))
    print(is_valid_email("@missing-local.com"))
    print(is_valid_email("user@.com"))