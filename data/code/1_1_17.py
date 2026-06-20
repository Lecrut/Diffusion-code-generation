import re

def _check_local_part_length(text):
    return len(text) <= 64

def _check_domain_parts(domain):
    if not domain:
        return False
    parts = domain.split('.')
    if len(parts) < 2:
        return False
    if parts[-1] == '':
        return False
    for part in parts:
        if not part:
            return False
        if len(part) > 63:
            return False
        if part[0] == '-' or part[-1] == '-':
            return False
    return True

def _check_double_dots(text):
    return '..' not in text

def validate_email(email):
    if not isinstance(email, str):
        return False
    if len(email) > 254:
        return False
    if not _check_double_dots(email):
        return False
    at_index = email.find('@')
    if at_index == -1:
        return False
    local_part = email[:at_index]
    domain_part = email[at_index + 1:]
    if not local_part or len(local_part) > 64:
        return False
    if not domain_part or domain_part.startswith('.') or domain_part.endswith('.'):
        return False
    if not _check_local_part_length(local_part):
        return False
    if not _check_double_dots(local_part):
        return False
    if not _check_double_dots(domain_part):
        return False
    local_pattern = re.compile(r'^[a-zA-Z0-9!#$%&\'*+/=?^_`{|}~-]+$', re.IGNORECASE)
    if not local_pattern.match(local_part):
        return False
    if not _check_domain_parts(domain_part):
        return False
    domain_pattern = re.compile(r'^[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*$')
    if not domain_pattern.match(domain_part):
        return False
    return True

if __name__ == '__main__':
    sample_inputs = [
        "alice@example.com",
        "bob.smith@sub.domain.co.uk",
        "charlie+test@server.net",
        "invalid@",
        "no-at-sign.com",
        "double..dots@test.com",
        "starts@.domain.com",
        "ends@domain.com.",
        "toolong" + "x" * 70 + "@test.com",
        "user@domain",
        "@missing.local",
        "valid@192.168.1.1"
    ]
    for test_email in sample_inputs:
        result = validate_email(test_email)
        print(f"{test_email}: {result}")