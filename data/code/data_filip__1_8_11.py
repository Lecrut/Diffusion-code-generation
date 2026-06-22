import re

def is_valid_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    if not email or len(email) > 254:
        return False
    if email.startswith('.') or email.endswith('.'):
        return False
    if '..' in email:
        return False
    local_part, _, domain_part = email.rpartition('@')
    if not local_part or not domain_part:
        return False
    if len(local_part) > 64:
        return False
    if domain_part.startswith('.') or domain_part.endswith('.'):
        return False
    if '..' in domain_part:
        return False
    domain_labels = domain_part.split('.')
    if len(domain_labels) < 2:
        return False
    for label in domain_labels:
        if not label or len(label) > 63:
            return False
        if label.startswith('-') or label.endswith('-'):
            return False
        if not re.match(r'^[A-Za-z0-9-]+$', label):
            return False
    local_pattern = r'^[a-zA-Z0-9!#$%&\'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&\'*+/=?^_`{|}~-]+)*$'
    if not re.match(local_pattern, local_part):
        return False
    return True

if __name__ == '__main__':
    test_cases = [
        "user@example.com",
        "user.name+tag@example.co.uk",
        "invalid.email@",
        "@example.com",
        "user@.com",
        "user@domain..com",
        "very.long.local.part.thats.goes.on.and.on.and.on.unless.it.exceeds.the.limit.of.sixty.four.characters.user@example.com",
        "-user@example.com",
        "user@-example.com",
        "user@example.c",
        "user name@example.com",
        "user@exam_ple.com"
    ]
    for email in test_cases:
        print(is_valid_email(email))