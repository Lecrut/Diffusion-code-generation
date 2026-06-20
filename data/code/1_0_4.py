import re
import socket
import socket.gaierror

EMAIL_REGEX = re.compile(
    r'^(?P<local>[a-zA-Z0-9!#$%&\'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&\'*+/=?^_`{|}~-]+)*)'
    r'@'
    r'(?P<domain>[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?)*)$'
)

def validate_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    match = EMAIL_REGEX.match(email)
    if not match:
        return False
    local_part = match.group('local')
    domain_part = match.group('domain')
    if not local_part or len(local_part) > 64:
        return False
    if len(local_part) > 64:
        return False
    if '.' in local_part:
        for segment in local_part.split('.'):
            if not segment:
                return False
            if segment[0] == '-' or segment[-1] == '-':
                return False
    if '.' in domain_part:
        domain_labels = domain_part.split('.')
        if not domain_labels or any(len(label) == 0 for label in domain_labels):
            return False
        if len(domain_labels) < 2:
            return False
        for label in domain_labels:
            if len(label) > 63:
                return False
            if label[0] == '-' or label[-1] == '-':
                return False
            if not all(c.isalnum() or c == '-' for c in label):
                return False
    else:
        if len(domain_part) > 255:
            return False
        if domain_part[0] == '-' or domain_part[-1] == '-':
            return False
        if not all(c.isalnum() or c == '-' for c in domain_part):
            return False
    return True

if __name__ == '__main__':
    test_emails = [
        "user@example.com",
        "user.name@sub.domain.co.uk",
        "invalid@",
        "@example.com",
        "user@.com",
        "user@domain..com",
        "user@-domain.com",
        "user@domain-",
        "user@domain.c",
        "user name@example.com",
        "user@ex ample.com",
        "valid+tag@domain.org"
    ]
    results = {}
    for email in test_emails:
        results[email] = validate_email(email)
    for email, is_valid in results.items():
        print(f"{email}: {is_valid}")