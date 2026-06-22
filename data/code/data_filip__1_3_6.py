import re

EMAIL_PATTERN = re.compile(
    r'^'
    r'(?P<local>[a-zA-Z0-9!#$%&\'*+\-/=?^_`{|}~]+'
    r'(?:\.[a-zA-Z0-9!#$%&\'*+\-/=?^_`{|}~]+)*)'
    r'@'
    r'(?P<domain>'
    r'(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+'
    r'[a-zA-Z]{2,}'
    r')'
    r'$'
)

def validate_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    return bool(EMAIL_PATTERN.match(email))

if __name__ == '__main__':
    samples = [
        "simple@example.com",
        "user.name+tag@sub.domain.org",
        "invalid-email@",
        "@no-local.com",
        "bad@domain.",
        "good@192.168.1.1",
        "a@b.c"
    ]
    for s in samples:
        print(f"{s}: {validate_email(s)}")