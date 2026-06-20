import re

_EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

def validate_email(email: str) -> bool:
    return bool(_EMAIL_PATTERN.match(email))

if __name__ == '__main__':
    valid_email = "user@example.com"
    invalid_email = "user@.com"
    print(validate_email(valid_email))
    print(validate_email(invalid_email))