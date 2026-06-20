import re

_email_regex = re.compile(
    r'^(?![.])'
    r'(?:(?![.-])'
    r'[a-zA-Z0-9.!#$%&\'*+/=?^_`{|}~-]'
    r'(?<![.-])'
    r'|'
    r'"(?:[^"\\]|\\.)*"'
    r')+'
    r'@'
    r'(?:'
    r'[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?'
    r'(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?)*'
    r'|'
    r'\[(?:[0-9]{1,3}\.){3}[0-9]{1,3}\]'
    r')$'
)

def validate_email(email):
    return bool(_email_regex.match(email))

if __name__ == '__main__':
    samples = [
        "user@example.com",
        "invalid.email",
        "user@.com",
        ".user@example.com",
        "user@-example.com",
        "user@example-.com",
        "user name@example.com",
        "user@sub.example.com",
        "test+tag@gmail.com",
        "user@[192.168.1.1]",
        "invalid@.com",
        "invalid@example..com"
    ]

    for sample in samples:
        print(f"{sample}: {validate_email(sample)}")