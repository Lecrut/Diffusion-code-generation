import re

EMAIL_PATTERN = re.compile(
    r'^[a-zA-Z0-9](?:[a-zA-Z0-9._%+-]*[a-zA-Z0-9])?@[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?)*\.[a-zA-Z]{2,}$'
)

def validate_email(email):
    return bool(email and EMAIL_PATTERN.match(email))

if __name__ == '__main__':
    samples = [
        "user@example.com",
        "first.last@domain.co.uk",
        "invalid@",
        "@missing.com",
        "no-at-sign.com",
        "user@.com",
        "user@domain",
        "",
        "user name@domain.com",
        "user+tag@domain.org",
        "u@b.co",
        "user@sub.domain.com",
        "user@123.123.123.com",
        "user@@domain.com",
        "user@domain..com",
        "user@domain.com.",
        ".user@domain.com",
        "user.@domain.com"
    ]

    results = [validate_email(email) for email in samples]
    for email, is_valid in zip(samples, results):
        print(f"{email!r}: {is_valid}")