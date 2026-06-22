import re

EMAIL_PATTERN = re.compile(r'^(?P<local>[a-zA-Z0-9_.+-]+)@(?P<domain>[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*)$')

def validate_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    return EMAIL_PATTERN.match(email) is not None

if __name__ == '__main__':
    test_addresses = [
        "user@example.com",
        "invalid.email",
        "test.user+tag@sub.domain.org",
        "@missinglocal.com",
        "no@domain",
        "spaces in email@test.com"
    ]
    
    for address in test_addresses:
        result = validate_email(address)
        print(f"{address}: {result}")