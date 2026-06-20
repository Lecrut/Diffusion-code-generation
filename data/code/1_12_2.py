import re

_email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

def validate_email(email: str) -> bool:
    return bool(_email_regex.match(email))

if __name__ == '__main__':
    result = validate_email('user@example.com')
    print(result)
    print(validate_email('invalid-email'))
    print(validate_email('another.test+tag@domain.org'))