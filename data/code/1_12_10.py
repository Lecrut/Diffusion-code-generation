import re

_email_pattern = re.compile(
    r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
)

def validate_email(email):
    if not isinstance(email, str):
        return False
    return _email_pattern.match(email) is not None

if __name__ == "__main__":
    test_cases = [
        "user@example.com",
        "invalid.email@",
        "@missing.com",
        "user.name+tag@domain.co.uk",
        "spaces in@email.com",
        "no-at-sign.com",
        "user@domain",
        "valid.email@sub.domain.org",
        "",
        12345
    ]
    for test in test_cases:
        result = validate_email(test)
        print(f"validate_email({repr(test)}) = {result}")