import re

def is_valid_email(email):
    if not isinstance(email, str):
        return False
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

if __name__ == '__main__':
    test_cases = [
        "user@example.com",
        "user.name+tag@domain.co.uk",
        "invalid-email@",
        "@missing-local.com",
        "no-at-symbol.com",
        "valid@sub.domain.com",
        "spaces @email.com",
        "double..dots@example.com",
        "underscore_test@domain.org",
        "capitals@UPPERCASE.COM"
    ]
    for test in test_cases:
        result = is_valid_email(test)
        print(f"{test}: {result}")