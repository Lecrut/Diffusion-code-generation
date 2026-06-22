import re

def validate_email(email):
    pattern = r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"
    match = re.match(pattern, email)
    if match:
        return True
    return False

if __name__ == '__main__':
    test_email = "user@example.com"
    invalid_email = "user@.com"
    valid = validate_email(test_email)
    invalid = validate_email(invalid_email)
    print(valid)
    print(invalid)