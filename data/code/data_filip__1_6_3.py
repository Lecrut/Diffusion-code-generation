import re

EMAIL_PATTERN = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

def validate_email(email: str) -> bool:
    return bool(EMAIL_PATTERN.match(email))

if __name__ == "__main__":
    test_cases = [
        "user@example.com",
        "user.name+tag@domain.co.uk",
        "invalid-email@",
        "@invalid.com",
        "missing@domain",
        "spaces @test.com",
        "valid@sub.domain.org"
    ]

    for email in test_cases:
        print(validate_email(email))