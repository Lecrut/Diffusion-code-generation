import re

COMPILED_EMAIL_PATTERN = re.compile(
    r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
)

def validate_email(email_address):
    return bool(COMPILED_EMAIL_PATTERN.match(email_address))

if __name__ == '__main__':
    test_cases = [
        "user@example.com",
        "user.name+tag@domain.co.uk",
        "invalid-email@",
        "@missing-local.com",
        "spaces in@email.com",
        "correct@email.com",
        "missing@domain",
        "double@@at.com"
    ]

    for case in test_cases:
        result = validate_email(case)
        print(f"{case}: {result}")