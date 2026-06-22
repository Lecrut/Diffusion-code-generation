import re

_EMAIL_PATTERN = re.compile(
    r'^[a-zA-Z0-9._%+-]+'
    r'@[a-zA-Z0-9.-]+'
    r'\.[a-zA-Z]{2,}$'
)

def is_valid_email_format(email: str) -> bool:
    if not isinstance(email, str):
        return False
    if not email:
        return False
    return bool(_EMAIL_PATTERN.match(email))

def validate_batch(emails: list) -> dict:
    results = {}
    for email in emails:
        results[email] = is_valid_email_format(email)
    return results

if __name__ == '__main__':
    sample_emails = [
        "admin@server.net",
        "test.user+filter@sub.domain.org",
        "invalid@",
        "@nolocal.com",
        "noatsign.com",
        "space in@local.com",
        "user@domain",
        "user@.com",
        "a@b.co",
        "complex_name-123@my-site.info"
    ]
    validation_results = validate_batch(sample_emails)
    for email, is_valid in validation_results.items():
        print(f"{email}: {is_valid}")