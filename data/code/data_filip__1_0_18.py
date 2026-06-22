import re

EMAIL_REGEX = re.compile(
    r'^[a-zA-Z0-9!#$%&\'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?'
    r'(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$'
)

def is_valid_email(address):
    if not isinstance(address, str) or not address:
        return False
    if EMAIL_REGEX.match(address):
        local, domain = address.rsplit('@', 1)
        if local.startswith('.') or local.endswith('.') or '..' in local:
            return False
        domain_parts = domain.split('.')
        if any(not part or part.startswith('-') or part.endswith('-') for part in domain_parts):
            return False
        return True
    return False

if __name__ == '__main__':
    samples = [
        "plain@example.com",
        "very.common@example.com",
        "disposable.style.email.with+symbol@example.com",
        "other.email-with-hyphen@example.com",
        "fully-qualified-domain@example.com",
        "user.name+tag+sorting@example.com",
        "x@example.com",
        "example-indeed@strange-example.com",
        "test@localhost",
        "123@123.com",
        "@nouser.com",
        "no_at_sign.com",
        "spaces in@email.com",
        "a.b@c.d",
        "valid@sub.domain.co.uk",
        "bad..dots@example.com",
        "bad-.domain.com",
        "-badlocal@example.com"
    ]
    results = [is_valid_email(e) for e in samples]
    print(dict(zip(samples, results)))