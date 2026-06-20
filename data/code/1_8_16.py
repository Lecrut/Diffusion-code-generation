import re

_EMAIL_REGEX = re.compile(
    r'^[a-zA-Z0-9.!#$%&\'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?'
    r'(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$'
)

def is_valid_email(email):
    if not isinstance(email, str):
        return False
    if len(email) > 254:
        return False
    if _EMAIL_REGEX.match(email):
        local_part, _, domain_part = email.partition('@')
        if len(local_part) > 64:
            return False
        return True
    return False

if __name__ == '__main__':
    test_cases = [
        "user@example.com",
        "invalid.email@",
        "@missinglocal.com",
        "user@.com",
        "user@com.",
        "user name@example.com",
        "valid.email+tag@subdomain.example.co.uk",
        "a@b.c",
        "toolong" * 20 + "@example.com",
        "user@-example.com",
        "user@exam_ple.com",
        "",
        "user@example.com ",
        " user@example.com",
        "user@example",
        "user@192.168.1.1",
    ]
    for email in test_cases:
        print(is_valid_email(email))