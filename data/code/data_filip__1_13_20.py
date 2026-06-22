import re

EMAIL_PATTERN = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

COMPILED_EMAIL_PATTERN = re.compile(EMAIL_PATTERN)

def validate_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    return bool(COMPILED_EMAIL_PATTERN.match(email))

if __name__ == '__main__':
    sample_emails = [
        "user@example.com",
        "invalid.email",
        "@missing-local.com",
        "no-at-sign.com",
        "valid+tag@domain.org",
        "simple@simple.com",
        "complex_name+tag@sub.domain.co.uk",
        "spaces in@email.com",
        ".start@bad.com",
        "end.@bad.com"
    ]
    
    results = [validate_email(email) for email in sample_emails]
    
    for email, is_valid in zip(sample_emails, results):
        print(f"{email}: {is_valid}")