import re

_pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

def is_valid_email(email: str) -> bool:
    return bool(_pattern.match(email))

if __name__ == '__main__':
    valid_email = "user@example.com"
    invalid_email = "user@.com"
    print(is_valid_email(valid_email))
    print(is_valid_email(invalid_email))