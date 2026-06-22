import re
import email.utils
import socket
import struct
_LOCAL_PART_PATTERN = re.compile('^[a-zA-Z0-9._%+-]+$')
_TLD_PATTERN = re.compile('^[a-zA-Z]{2,}$')

def validate_email(email_str: str) -> bool:
    if not isinstance(email_str, str):
        return False
    email_str = email_str.strip()
    if not email_str:
        return False
    if email_str.count('@') != 1:
        return False
    local_part, domain_part = email_str.rsplit('@', 1)
    if len(local_part) < 1 or len(local_part) > 64:
        return False
    if len(domain_part) < 1 or len(domain_part) > 255:
        return False
    if not _LOCAL_PART_PATTERN.match(local_part):
        return False
    if '..' in local_part:
        return False
    if not domain_part or domain_part.startswith('-') or domain_part.endswith('-'):
        return False
    if '.' not in domain_part:
        return False
    labels = domain_part.split('.')
    for label in labels:
        if not label:
            return False
        if len(label) > 63:
            return False
        if not re.match('^[a-zA-Z0-9]([a-zA-Z0-9-]*[a-zA-Z0-9])?$', label):
            return False
    tld = labels[-1]
    if not _TLD_PATTERN.match(tld) or len(tld) < 2:
        return False
    return True

def is_domain_valid(domain: str) -> bool:
    try:
        addr_info = socket.getaddrinfo(domain, None, socket.AF_INET)
        return len(addr_info) > 0
    except socket.gaierror:
        return False
if __name__ == '__main__':
    samples = ['user@example.com', 'invalid-email', 'user@-invalid.com', 'user@192.168.1.1', 'user+tag@example.co.uk', '', 'user name@example.com', 'user@com', 'user@.example.com', 'user@example.c', 'normal.user+tag@domain.org']
    results = []
    for sample in samples:
        results.append(validate_email(sample))
    print(results)