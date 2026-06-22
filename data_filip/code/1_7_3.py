import re

_EMAIL_PATTERN = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

def is_valid_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    return bool(_EMAIL_PATTERN.match(email))

if __name__ == '__main__':
    test_email = "user@example.com"
    print(is_valid_email(test_email))