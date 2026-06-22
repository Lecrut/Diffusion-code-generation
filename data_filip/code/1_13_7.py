import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_emails(email_list):
    return [validate_email(email) for email in email_list]

if __name__ == '__main__':
    sample_emails = [
        "user@example.com",
        "invalid.email@",
        "test@domain.co.uk",
        "@missing.com",
        "valid.name+tag@site.org",
        "spaces in@email.com",
        "no-at-sign.com",
        "multiple@@signs.com",
        "user@.com",
        "user@com.",
        "a@b.c",
        "very.common@example.org",
        "disposable.style.email.with+symbol@example.com",
        "other.email-with-hyphen@example.com",
        "fully-qualified-domain@example.com",
        "user.name+tag+sorting@example.com",
        "x@example.com",
        "example-indeed@strange-host.name",
        "example@s.solutions",
        "user@localhost",
        "user@[127.0.0.1]"
    ]
    results = validate_emails(sample_emails)
    for email, is_valid in zip(sample_emails, results):
        print(f"{email}: {is_valid}")