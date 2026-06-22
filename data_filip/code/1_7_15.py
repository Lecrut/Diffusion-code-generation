import re

def is_valid_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

if __name__ == '__main__':
    test_cases = [
        "user@example.com",
        "user.name@domain.co.uk",
        "invalid-email@",
        "@missing-user.com",
        "user@.com",
        "user@domain",
        "another_valid@test.org"
    ]
    for case in test_cases:
        print(f"{case}: {is_valid_email(case)}")