import re

compiled_pattern = re.compile(
    r"^(?P<local>[a-zA-Z0-9_.+-]+)"
    r"@"
    r"(?P<domain>[a-zA-Z0-9-]+)"
    r"(?:\.(?P=sublocal)?[a-zA-Z0-9-]+)*$"
)

def validate_email(email):
    return compiled_pattern.match(email) is not None

if __name__ == '__main__':
    test_cases = [
        "user@example.com",
        "john.doe+filter@sub.domain.co.uk",
        "invalid-email@",
        "@missing-local.com",
        "no-at-sign.com",
        "spaces in@email.com",
        "double@@at.com",
        "user@-leadingdash.com",
        "user@domain..com",
        "valid_user@domain-name.org"
    ]

    for case in test_cases:
        result = validate_email(case)
        print(f"{case}: {result}")