import re

_EMAIL_PATTERN = re.compile(
    r"^(?P<local>[a-zA-Z0-9_.+-]+)@"
    r"(?P<domain>[a-zA-Z0-9-]+)"
    r"(?:\.[a-zA-Z0-9-]+)*$"
)

def validate_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    if not email or len(email) > 254:
        return False
    return bool(_EMAIL_PATTERN.match(email))

if __name__ == "__main__":
    test_cases = [
        "user@example.com",
        "invalid.email@",
        "another@invalid",
        "name.with.dots+tag@sub.domain.co",
        "bad..chars@example.com",
        None,
        "",
        "a" * 255 + "@example.com",
        "valid.user@server.org"
    ]
    for case in test_cases:
        result = validate_email(case)
        print(f"{repr(case):<35} -> {result}")