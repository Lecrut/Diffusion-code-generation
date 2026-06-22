import re

DOMAIN_TLD_MIN_LENGTH = 2
LOCAL_PART_MIN_LENGTH = 1

COMPILED_PATTERN = re.compile(
    r'^(?=' + '.'.join([
        r'.{3,254}$',
        r'[^@]+@[^@]+'
    ]) + r')'
    r'(?!.*\.\.)'
    r'(?!^[^.@])'
    r'(?!.*@[^.])'
    r'[a-zA-Z0-9_.+-]+'
    r'@'
    r'(?=.*[a-zA-Z0-9-])'
    r'[a-zA-Z0-9-]+'
    r'(?:\.[a-zA-Z0-9-]+)*'
    r'\.'
    r'([a-zA-Z0-9-]+)'
    r'$'
)

def validate_domain_part(domain):
    if '.' not in domain:
        return False
    parts = domain.split('.')
    if len(parts) < 2:
        return False
    tld = parts[-1]
    if len(tld) < DOMAIN_TLD_MIN_LENGTH:
        return False
    return True

def check_email_syntax(email):
    if not isinstance(email, str):
        return False
    if email.count('@') != 1:
        return False
    local, domain = email.rsplit('@', 1)
    if len(local) < LOCAL_PART_MIN_LENGTH:
        return False
    if not domain:
        return False
    match = COMPILED_PATTERN.match(email)
    if not match:
        return False
    if not validate_domain_part(domain):
        return False
    return True

if __name__ == '__main__':
    test_cases = [
        "john.doe@example.com",
        "support+help@company.co.uk",
        "bad..double@domain.com",
        "@start.with.dot.com",
        "user@nodot",
        "user@domain.c",
        "simple@valid.org",
        "user@sub.domain.info"
    ]
    for item in test_cases:
        result = check_email_syntax(item)
        print(result)