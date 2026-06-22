import re

LOCAL_PART_PATTERN = r'[a-zA-Z0-9._%+-]+'
DOMAIN_PATTERN = r'[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+'
TLD_PATTERN = r'[a-zA-Z]{2,}'
MAX_LENGTH = 254
MIN_LOCAL_LENGTH = 1
MIN_DOMAIN_LENGTH = 4

def check_length(email):
    if not isinstance(email, str):
        return False
    if len(email) > MAX_LENGTH:
        return False
    if len(email) < MIN_LOCAL_LENGTH + 1 + MIN_DOMAIN_LENGTH:
        return False
    return True

def validate_structure(email):
    if not check_length(email):
        return False
    pattern = re.compile(
        r'^'
        r'(?=.*@)'
        r'(?=.*\.)'
        r'(?!(.*@.*@))'
        r'(?!(.*\.\..*))'
        r'(?!(^\.))'
        r'(?!(.*\.$))'
        r'(' + LOCAL_PART_PATTERN + r')'
        r'@'
        r'(' + DOMAIN_PATTERN + r')'
        r'\.'
        r'(' + TLD_PATTERN + r')'
        r'$'
    )
    match = pattern.match(email)
    if not match:
        return False
    domain_part = match.group(2) + '.' + match.group(3)
    domain_sections = domain_part.split('.')
    if len(domain_sections) < 2:
        return False
    for section in domain_sections:
        if len(section) == 0 or len(section) > 63:
            return False
        if section.startswith('-') or section.endswith('-'):
            return False
    return True

def validate_email(email):
    return validate_structure(email)

if __name__ == '__main__':
    test_cases = [
        "alice@example.com",
        "bob.smith+filter@sub.domain.co.uk",
        "bad@",
        "@bad.com",
        "no-at.com",
        "double..dot@test.com",
        "valid@sub-domain.org",
        "user@domain.c",
        "very.long.email.address.with.many.parts@example-domain.org"
    ]
    results = {}
    for test_email in test_cases:
        results[test_email] = validate_email(test_email)
    for email_val, is_valid in results.items():
        print(email_val, is_valid)