import re

EMAIL_REGEX = re.compile(
    r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
)

def validate_email(email):
    return bool(EMAIL_REGEX.match(email))

if __name__ == '__main__':
    sample_emails = [
        "user@example.com",
        "invalid.email",
        "@missing-user.com",
        "user@",
        "user@.com",
        "user@sub.domain.com",
        "user name@example.com",
        "user@exam ple.com",
        "user@192.168.1.1",
        "valid+tag@example.co.uk",
        "a@b.c",
        "test@domain",
        "test@domain.",
        "test..test@domain.com",
        "test@domain.c",
        "test@domain.co",
        "test@domain..com",
        "test@domain.com.",
        ".test@domain.com",
        "test.@domain.com",
        "test@domain.com ",
        " test@domain.com",
        "test@domain.com\n",
        "test@domain.com\r",
        "test@domain.com\t",
        "test@domain.com  ",
        "test@domain.com  test"
    ]

    results = []
    for email in sample_emails:
        is_valid = validate_email(email)
        results.append(f"Email: '{email}' is {'Valid' if is_valid else 'Invalid'}")

    for result in results:
        print(result)