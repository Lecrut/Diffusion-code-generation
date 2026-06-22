import re
from typing import List, Tuple

EMAIL_PATTERN = re.compile(
    r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
)

def validate_emails(emails: List[str]) -> List[Tuple[str, bool]]:
    results = []
    for email in emails:
        is_valid = bool(EMAIL_PATTERN.match(email))
        results.append((email, is_valid))
    return results

if __name__ == '__main__':
    sample_emails = [
        "user@example.com",
        "invalid.email",
        "@missing-local.com",
        "no-at-sign.com",
        "valid+tag@sub.domain.org",
        "spaces in@email.com",
        "user@.com",
        "user@domain..com",
        "simple@example.org",
        "very.common@example.com",
        "disposable.style.email.with+symbol@example.com",
        "other.email-with-hyphen@example.com",
        "fully-qualified-domain@example.com",
        "user.name+tag+sorting@example.com",
        "x@example.com",
        "example-indeed@strange-example.com",
        "test.email.with@dot.example.com",
        "example@s.example",
        "user-123@gitlab.com",
        "admin@local-server"
    ]

    validation_results = validate_emails(sample_emails)
    print(validation_results)