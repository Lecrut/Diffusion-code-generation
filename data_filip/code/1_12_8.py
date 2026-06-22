import re

_PATTERN = re.compile(
    r'^(?P<local>[a-zA-Z0-9_.+-]+)@'
    r'(?P<domain>[a-zA-Z0-9-]+'
    r'(?:\.[a-zA-Z0-9-]+)*)$'
)

def validate_email(email: str) -> bool:
    return _PATTERN.match(email) is not None

if __name__ == '__main__':
    samples = [
        "user@example.com",
        "invalid.email@com",
        "test.user+tag@sub.domain.org",
        "@no-local.com",
        "no-at-symbol.com"
    ]
    for s in samples:
        print(f"{s}: {validate_email(s)}")