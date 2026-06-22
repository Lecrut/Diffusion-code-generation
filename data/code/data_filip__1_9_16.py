import re

def validate_email_format(email):
    if not isinstance(email, str):
        return False
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

if __name__ == '__main__':
    test_cases = [
        "user@example.com",
        "user.name@sub.domain.co.uk",
        "invalid-email@",
        "@domain.com",
        "missing@.com",
        "spaces in email@test.com",
        "valid+tag@server.org"
    ]
    for case in test_cases:
        print(validate_email_format(case))