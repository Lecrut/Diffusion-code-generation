import re
import email.utils

def is_valid_email(address):
    if not isinstance(address, str):
        return False
    if len(address) > 320:
        return False
    if not address or address.startswith('.') or address.endswith('.'):
        return False
    if address.count('@') != 1:
        return False
    local_part, domain_part = address.rsplit('@', 1)
    if not local_part or not domain_part:
        return False
    if len(local_part) > 64:
        return False
    if len(domain_part) > 255:
        return False
    if domain_part.startswith('.') or domain_part.endswith('.'):
        return False
    if '..' in local_part or '..' in domain_part:
        return False
    local_pattern = r'^[a-zA-Z0-9!#$%&\'*+/=?^_`{|}~-]+(\.[a-zA-Z0-9!#$%&\'*+/=?^_`{|}~-]+)*$'
    if not re.match(local_pattern, local_part):
        if not re.match(r'^"[^"\\]*(\\.[^"\\]*)*"$', local_part):
            return False
    domain_label_pattern = r'^[a-zA-Z0-9]([a-zA-Z0-9-]*[a-zA-Z0-9])?$'
    if len(domain_part) > 255:
        return False
    if '.' not in domain_part:
        if not re.match(domain_label_pattern, domain_part):
            return False
    else:
        labels = domain_part.split('.')
        if labels[-1] == '':
            return False
        for label in labels:
            if not label:
                return False
            if len(label) > 63:
                return False
            if not re.match(domain_label_pattern, label):
                return False
    try:
        parsed = email.utils.parseaddr(address)
        if parsed[1] == '' or parsed[1] != address:
            return False
    except Exception:
        return False
    return True

if __name__ == '__main__':
    test_cases = [
        "user@example.com",
        "invalid.email",
        "@example.com",
        "user@.com",
        "user..name@example.com",
        "user@exa_mple.com",
        "user@sub.domain.com",
        "user+tag@example.co.uk",
        "very.cause@example",
        "name with space@example.com",
        "user@[192.168.1.1]"
    ]
    for email_addr in test_cases:
        result = is_valid_email(email_addr)
        print(f"{email_addr}: {result}")