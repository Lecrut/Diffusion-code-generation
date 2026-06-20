import re

_email_pattern = re.compile(
    r'^(?P<local>[a-zA-Z0-9._%+-]+)@'
    r'(?P<domain>[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$'
)

def validate_email(email: str) -> bool:
    return bool(_email_pattern.match(email))

if __name__ == '__main__':
    test_cases = [
        "user@example.com",
        "user.name+tag@domain.co.uk",
        "invalid-email@",
        "@domain.com",
        "user@domain",
        "user@domain.c",
        "user@@domain.com",
        "user name@domain.com",
        "user@domain..com",
        "valid_email@sub.domain.org"
    ]

    for case in test_cases:
        result = validate_email(case)
        print(f"{case}: {result}")