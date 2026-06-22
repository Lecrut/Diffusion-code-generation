import re

_EMAIL_REGEX = re.compile(
    r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
)

_MAX_LOCAL_LENGTH = 64
_MAX_DOMAIN_LENGTH = 253
_MAX_EMAIL_LENGTH = 254

def _check_length_constraints(email):
    return len(email) <= _MAX_EMAIL_LENGTH

def _split_email(email):
    at_index = email.rfind('@')
    if at_index == -1:
        return None, None
    local_part = email[:at_index]
    domain_part = email[at_index + 1:]
    if not local_part or not domain_part:
        return None, None
    return local_part, domain_part

def _validate_local_part(local):
    if len(local) > _MAX_LOCAL_LENGTH:
        return False
    if local.startswith('.') or local.endswith('.'):
        return False
    if '..' in local:
        return False
    return True

def _validate_domain_part(domain):
    if len(domain) > _MAX_DOMAIN_LENGTH:
        return False
    if domain.startswith('-') or domain.endswith('-'):
        return False
    if '..' in domain:
        return False
    labels = domain.split('.')
    for label in labels:
        if not label:
            return False
        if label.startswith('-') or label.endswith('-'):
            return False
        if not re.match(r'^[a-zA-Z0-9-]+$', label):
            return False
    if len(labels) < 2:
        return False
    tld = labels[-1]
    if not re.match(r'^[a-zA-Z]{2,}$', tld):
        return False
    return True

def validate_email_format(email):
    if not isinstance(email, str):
        return False
    if not _check_length_constraints(email):
        return False
    if not _EMAIL_REGEX.match(email):
        return False
    local_part, domain_part = _split_email(email)
    if local_part is None:
        return False
    if not _validate_local_part(local_part):
        return False
    if not _validate_domain_part(domain_part):
        return False
    return True

def run_tests():
    test_cases = [
        ("user@example.com", True),
        ("first.last@domain.co.uk", True),
        ("user+tag@sub.domain.org", True),
        ("invalid.email@", False),
        ("@missinglocal.com", False),
        ("missingat.com", False),
        ("double@@at.com", False),
        ("spaces in email@test.com", False),
        ("user@.com", False),
        ("user@domain.c", False),
        ("valid.email.name@domain.com", True),
        ("a@b.co", True),
        ("user@domain..com", False),
        ("user@-domain.com", False),
        ("user@domain-.com", False),
        (".user@domain.com", False),
        ("user.@domain.com", False),
        ("user@domain", False),
    ]
    results = []
    for email, expected in test_cases:
        actual = validate_email_format(email)
        results.append((email, expected, actual))
    return results

if __name__ == '__main__':
    test_results = run_tests()
    for email, expected, actual in test_results:
        print(f"{email}: expected={expected}, got={actual}, pass={expected == actual}")