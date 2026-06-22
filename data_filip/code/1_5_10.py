import re

_email_pattern = re.compile(r"^(?!.*\.\.)(?!.*\.$)(?!(?<=@)\.)[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

def validate_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    return bool(_email_pattern.match(email))

if __name__ == '__main__':
    test_cases = [
        "user@example.com",
        "user.name+tag@sub.domain.org",
        "invalid-email@",
        "@invalid.com",
        "user..name@example.com",
        "user@.com",
        "valid_user123@test-domain.co.uk",
        ""
    ]
    for case in test_cases:
        print(f"{case}: {validate_email(case)}")