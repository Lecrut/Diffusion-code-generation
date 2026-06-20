import re

_email_pattern = re.compile(
    r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
)

def validate_email(email: str) -> bool:
    return bool(_email_pattern.match(email))

if __name__ == '__main__':
    test_emails = [
        "user@example.com",
        "first.last@domain.org",
        "user+tag@domain.co",
        "user@sub.domain.com",
        "invalid@.com",
        "@nodomain.com",
        "no_at_symbol.com",
        "user@domain",
        "spaces in@email.com",
        "user@domain..com"
    ]
    
    results = {email: validate_email(email) for email in test_emails}
    print(results)