import re

EMAIL_REGEX = re.compile(
    r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
)

def validate_email(email):
    return bool(EMAIL_REGEX.match(email))

def validate_emails(emails):
    return [validate_email(email) for email in emails]

if __name__ == '__main__':
    sample_emails = [
        "user@example.com",
        "invalid-email",
        "user.name+tag@example.co.uk",
        "@missing-local.com",
        "no-at-sign.com",
        "spaces in@email.com",
        "valid.email@domain.museum",
        "user@.com",
        "user@domain.",
        "",
        "a@b.c",
        "very.common@example.org",
        "disposable.style.email.with+symbol@example.com",
        "other.email-with-hyphen@example.com",
        "fully-qualified-domain@example.com",
        "user.name+tag+sorting@example.com",
        "x@example.com",
        "example-indeed@strange-example.com",
        "test@localhost",
        "1234567890@example.com",
        "email@example.museum"
    ]
    results = validate_emails(sample_emails)
    for email, is_valid in zip(sample_emails, results):
        print(f"{email}: {is_valid}")