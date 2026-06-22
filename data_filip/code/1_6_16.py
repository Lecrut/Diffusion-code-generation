import re

EMAIL_PATTERN = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

def validate_email(email: str) -> bool:
    return bool(EMAIL_PATTERN.match(email))

if __name__ == "__main__":
    test_cases = [
        "user@example.com",
        "user.name+tag@domain.co.uk",
        "invalid-email@",
        "@missing-local.com",
        "no-at-symbol.com",
        "user@domain",
        "another.valid@email.org",
        "bad..dots@site.com",
    ]

    results = []
    for case in test_cases:
        results.append((case, validate_email(case)))

    for email, is_valid in results:
        print(f"{email}: {is_valid}")