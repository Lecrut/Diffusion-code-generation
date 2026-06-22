import re

EMAIL_REGEX = re.compile(
    r"^(?P<local>[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)*)@"
    r"(?P<domain>(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,})$"
)

def is_valid_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    if len(email) > 254:
        return False
    if email.count('@') != 1:
        return False
    return EMAIL_REGEX.match(email) is not None

if __name__ == '__main__':
    test_cases = [
        "user@example.com",
        "user.name@sub.domain.com",
        "invalid-email@",
        "@missing-local.com",
        "user@invalid",
        "user+tag@domain.co.uk",
        "user@domain.c",
        "user..name@domain.com",
        "valid@example.org",
        "user_name@domain.net"
    ]
    
    for email in test_cases:
        result = is_valid_email(email)
        print(f"{email}: {result}")