import re

_email_pattern = re.compile(
    r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
)

def validate_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    if len(email) > 254:
        return False
    if '@' not in email:
        return False
    if email.startswith('.') or email.endswith('.'):
        return False
    if '..' in email:
        return False
    if email.count('@') != 1:
        return False
    if email.startswith('-') or email.endswith('-'):
        return False
    if email.startswith('.') or email.endswith('.'):
        return False
    if not _email_pattern.match(email):
        return False
    local, domain = email.rsplit('@', 1)
    if len(local) > 64:
        return False
    if domain.startswith('-') or domain.endswith('-'):
        return False
    return True

if __name__ == '__main__':
    samples = [
        "user@example.com",
        "invalid@.com",
        "user@domain.co.uk",
        "bad@@example.com",
        "user name@example.com",
        "user@example",
        "test+tag@domain.org",
        "",
        "a@b.c",
        "user@-domain.com",
        "user@domain-.com",
        "user@domain..com",
        "user.name@sub.domain.com",
        "invalid user@example.com",
        "user@192.168.1.1",
    ]
    results = [validate_email(s) for s in samples]
    for s, r in zip(samples, results):
        print(f"{s}: {r}")