import re

EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

def validate_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    return bool(EMAIL_PATTERN.match(email))

if __name__ == '__main__':
    test_email = "user@example.com"
    result = validate_email(test_email)
    print(result)