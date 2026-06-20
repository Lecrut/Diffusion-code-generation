import re

EMAIL_REGEX = re.compile(
    r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"
)

def validate_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    return bool(EMAIL_REGEX.fullmatch(email))

if __name__ == '__main__':
    test_email = "user@example.com"
    invalid_email = "user@.com"
    result_valid = validate_email(test_email)
    result_invalid = validate_email(invalid_email)
    print(result_valid)
    print(result_invalid)