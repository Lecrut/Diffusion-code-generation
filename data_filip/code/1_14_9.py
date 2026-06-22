import re

EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

def validate_email(email: str) -> bool:
    return bool(EMAIL_PATTERN.match(email))

if __name__ == '__main__':
    test_cases = [
        "user@example.com",
        "user.name+tag@domain.co.uk",
        "invalid-email@",
        "another@invalid",
        "no-at-symbol.com",
        "valid_user123@test.org",
        "bad@domain.c",
        "spaces in@email.com",
        "double@@at.com",
        "ok@sub.domain.net"
    ]

    for case in test_cases:
        result = validate_email(case)
        print(f"{case}: {result}")