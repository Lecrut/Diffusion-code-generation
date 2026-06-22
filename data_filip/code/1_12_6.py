import re

_EMAIL_PATTERN = re.compile(
    r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
)

def validate_email(email: str) -> bool:
    return bool(_EMAIL_PATTERN.match(email))

if __name__ == '__main__':
    sample_emails = [
        "user@example.com",
        "invalid-email",
        "test.user+tag@domain.co.uk",
        "@missinguser.com",
        "no_at_sign.com",
        "spaces in@email.com"
    ]
    
    results = [validate_email(email) for email in sample_emails]
    print(results)