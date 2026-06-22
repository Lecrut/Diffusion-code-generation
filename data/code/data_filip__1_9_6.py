import re

def validate_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

if __name__ == '__main__':
    print(validate_email("user@example.com"))
    print(validate_email("invalid-email"))
    print(validate_email("test+tag@domain.co.uk"))