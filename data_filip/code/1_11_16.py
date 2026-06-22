import re

def validate_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

if __name__ == '__main__':
    test_cases = [
        "user@example.com",
        "invalid.email@",
        "another.user@domain.co.uk",
        "bad-format@domain",
        ""
    ]
    for case in test_cases:
        result = validate_email(case)
        print(f"{case}: {result}")