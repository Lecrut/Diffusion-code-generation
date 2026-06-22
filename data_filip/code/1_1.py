import re

def is_valid_email(email):
    pattern = re.compile(
        r'^'
        r'(?=.{6,254}$)'
        r'(?=.*\.)'
        r'(?![.][.]*)'
        r'([a-zA-Z0-9_.+-]+)'
        r'@'
        r'([a-zA-Z0-9-]+)'
        r'(\.[a-zA-Z0-9-]+)*'
        r'\.'
        r'[a-zA-Z0-9-]{2,}'
        r'$'
    )
    return bool(pattern.match(email))

if __name__ == '__main__':
    emails = ["user@example.com", "invalid@", "test.user@domain.co.uk", "no-at-sign.com", "@missing.com"]
    for email in emails:
        result = is_valid_email(email)
        print(f"{email}: {result}")