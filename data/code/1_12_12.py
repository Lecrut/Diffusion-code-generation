import re

EMAIL_REGEX = re.compile(
    r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
)

def validate_email(email):
    if not isinstance(email, str):
        return False
    return EMAIL_REGEX.match(email) is not None

if __name__ == '__main__':
    sample_emails = [
        "user@example.com",
        "invalid.email",
        "user@.com",
        "user@com.",
        "user name@example.com",
        "valid.email+tag@sub.domain.org",
        "",
        "user@localhost",
        "user@192.168.1.1"
    ]
    results = [validate_email(email) for email in sample_emails]
    for email, is_valid in zip(sample_emails, results):
        print(f"{email}: {is_valid}")