import re

_email_pattern = re.compile(
    r'^(?P<local>[a-zA-Z0-9_.+-]+)'
    r'@'
    r'(?P<domain>[a-zA-Z0-9-]+'
    r'(?:\.[a-zA-Z0-9-]+)*)'
    r'\.[a-zA-Z]{2,}$'
)

def is_valid_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    if not email:
        return False
    return _email_pattern.match(email) is not None

if __name__ == '__main__':
    test_cases = [
        "user@example.com",
        "user.name+tag@domain.co.uk",
        "invalid-email@",
        "another@invalid",
        "spaces in email@test.com",
        "missing@domain.",
        "valid123@test-domain.org",
        "@no-local.com",
        "no-at-sign.com",
        "double@@at.com"
    ]
    
    for case in test_cases:
        result = is_valid_email(case)
        print(f"{case}: {result}")