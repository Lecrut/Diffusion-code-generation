import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

def validate_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    return EMAIL_REGEX.match(email) is not None

if __name__ == '__main__':
    emails = ["user@example.com", "invalid.email", "test+tag@domain.org", "no-at-sign.com"]
    results = {email: validate_email(email) for email in emails}
    print(results)