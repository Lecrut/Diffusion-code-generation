import re

def is_valid_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    pattern = re.compile(
        r"^(?P<local>[a-zA-Z0-9_.+-]+)"
        r"@"
        r"(?P<domain>[a-zA-Z0-9-]+\."
        r"(?:[a-zA-Z0-9-]+\.)?[a-zA-Z]{2,})$"
    )
    return pattern.match(email) is not None

if __name__ == '__main__':
    test_emails = [
        "user@example.com",
        "firstname.lastname@domain.co.uk",
        "invalid.email@",
        "@domain.com",
        "user@domain",
        "user+tag@example.org",
        "bad..char@test.com"
    ]
    for address in test_emails:
        result = is_valid_email(address)
        print(f"{address}: {result}")