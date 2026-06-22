import re

_email_pattern = re.compile(
    r"^(?P<local>[a-zA-Z0-9._%+-]+)"
    r"@"
    r"(?P<domain>[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$"
)

def is_valid_email(email: str) -> bool:
    return bool(_email_pattern.match(email))

if __name__ == "__main__":
    test_cases = [
        "user@example.com",
        "first.last@domain.co.uk",
        "user+tag@sub.domain.org",
        "invalid.email@",
        "@missinglocal.com",
        "missingat.com",
        "double@@at.com",
        "spaces in email@test.com",
        "good_name@123.456",
        "valid@test.museum",
        "a@b.c"
    ]

    results = []
    for case in test_cases:
        results.append(is_valid_email(case))

    for i, res in enumerate(results):
        print(f"{test_cases[i]}: {res}")