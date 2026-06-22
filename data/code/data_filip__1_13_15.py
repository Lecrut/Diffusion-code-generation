import re
from typing import List, Tuple

EMAIL_REGEX = re.compile(
    r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
)

def validate_emails(email_list: List[str]) -> Tuple[List[str], List[str]]:
    valid = []
    invalid = []
    for email in email_list:
        if isinstance(email, str) and EMAIL_REGEX.match(email):
            valid.append(email)
        else:
            invalid.append(email)
    return valid, invalid

if __name__ == '__main__':
    emails = [
        "user@example.com",
        "invalid.email",
        "test+tag@sub.domain.org",
        "@missing.com",
        "no-at-sign.com",
        "user@.com",
        "user@com",
        "double..dot@example.com",
        "normal.user@example.co.uk",
        "UPPERCASE@EXAMPLE.COM",
        "user name@example.com",
        "user@exam ple.com",
        "user@exam..ple.com",
        "user@-example.com",
        "user@example-.com",
        "u@b.cd",
        "very.common@example.com",
        "disposable.style.email.with+symbol@example.com",
        "other.email-with-hyphen@example.com",
        "fully-qualified-domain@example.com",
        "user.name+tag+sorting@example.com",
        "x@example.com",
        "example-indeed@strange-example.com",
        "test/test@test.com",
        "1234567890@example.com",
        "admin@mail-server.example.org",
        "postmaster@example.net",
        "www@example.info",
        "_test@localhost",
        "test@local",
        "test@localhost.",
        ".invalid@example.com",
        "invalid.@example.com",
        "invalid..invalid@example.com",
        "invalid@example..com",
        "invalid@example.com.",
        "inv@lid@example.com",
        "inv@.example.com",
        "inv@example..com",
        "inv@example.c",
        "inv@example.123",
        "inv@example.com.",
        " inv@example.com",
        "inv@example.com ",
        "",
        None,
        123,
    ]
    result = validate_emails(emails)
    print(result)