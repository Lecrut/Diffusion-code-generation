import re

EMAIL_REGEX = re.compile(
    r'^[a-zA-Z0-9.!#$%&\'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?'
    r'(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$'
)

def validate_email(email):
    if not isinstance(email, str):
        return False
    return bool(EMAIL_REGEX.match(email))

if __name__ == '__main__':
    sample_emails = [
        "user@example.com",
        "invalid@",
        "@invalid.com",
        "user.name+tag@domain.co.uk",
        "a@b",
        "spaces in@email.com",
        "user@.com",
        "user@domain.c",
        "",
        "user@domain..com"
    ]
    results = [validate_email(email) for email in sample_emails]
    print(results)