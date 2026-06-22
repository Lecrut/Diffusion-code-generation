import re
import sys

_EMAIL_REGEX = re.compile(
    r'^[a-zA-Z0-9](?:[a-zA-Z0-9._+-]*[a-zA-Z0-9])?@[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.[a-zA-Z]{2,}$'
)

def validate_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    if len(email) > 254:
        return False
    if _EMAIL_REGEX.match(email):
        local, domain = email.rsplit("@", 1)
        if len(local) > 64:
            return False
        if not domain:
            return False
        return True
    return False

if __name__ == '__main__':
    test_cases = [
        ("user@example.com", True),
        ("first.last@domain.org", True),
        ("email+tag@example.net", True),
        ("1234567890@example.com", True),
        ("user@sub.domain.co.uk", True),
        ("plainaddress", False),
        ("@missing.com", False),
        ("missing@.com", False),
        ("missing@com.", False),
        ("spaces in@email.com", False),
        ("double@@email.com", False),
        ("invalid~char@email.com", False),
        ("", False),
        (None, False),
        (12345, False),
    ]

    results = []
    for email, expected in test_cases:
        result = validate_email(email)
        results.append((email, expected, result))

    print(results)