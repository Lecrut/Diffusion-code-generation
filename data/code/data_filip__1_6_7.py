import re

def is_valid_email(email):
    pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    if email is None or not isinstance(email, str):
        return False
    return bool(pattern.match(email))

if __name__ == '__main__':
    test_emails = [
        "user@example.com",
        "first.last@domain.org",
        "user+tag@example.co.uk",
        "user@sub.domain.com",
        "invalid@",
        "@invalid.com",
        "no-at-sign.com",
        "spaces in@email.com",
        "user@.com",
        "user@domain",
        "user@domain..com",
        "user_name@domain.org",
        "1234567890@1234567890.com"
    ]
    
    for email in test_emails:
        result = is_valid_email(email)
        print(f"{email}: {result}")