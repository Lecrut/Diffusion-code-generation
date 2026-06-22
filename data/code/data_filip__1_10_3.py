import re

_EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

def validate_email(email: str) -> bool:
    return bool(_EMAIL_PATTERN.match(email))

if __name__ == '__main__':
    results = [
        validate_email("user@example.com"),
        validate_email("invalid.email"),
        validate_email("test+tag@domain.co.uk"),
        validate_email("@missing.com"),
    ]
    print(results)