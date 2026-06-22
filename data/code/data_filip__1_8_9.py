import re
import socket
import string
EMAIL_MAX_LENGTH = 254
LOCAL_PART_MAX = 64
DOMAIN_PART_MAX = 253
SPECIAL_CHARS_LOCAL = "!#$%&'*+/=?^_`{|}~"
DOT_START_END = ('start', 'end')
DOUBLE_DOT = '..'
DOT_SEPARATOR = '.'
_LOCAL_PART_RE = re.compile("^(?:(?:[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+\\.)+(?:[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)|[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)$")
_LOCAL_PATTERN_STR = "^(?!.*\\.\\.|^\\.$)(?!^\\.)([a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+(\\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)*)$"
_DOMAIN_LABEL_RE = re.compile('^[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?$')
_IPv4_RE = re.compile('^\\[(?:\\d{1,3}\\.){3}\\d{1,3}\\]$')
_IPV6_TAG_RE = re.compile('^\\[v6?:[0-9a-fA-F:]+\\]$')

def _is_valid_ipv4_address(ip_str: str) -> bool:
    try:
        socket.inet_pton(socket.AF_INET, ip_str)
        return True
    except Exception:
        return False

def _is_valid_domain(domain: str) -> bool:
    if not domain:
        return False
    if len(domain) > DOMAIN_PART_MAX:
        return False
    if domain.startswith('.') or domain.endswith('.'):
        return False
    if domain.startswith('['):
        if domain.endswith(']'):
            inner = domain[1:-1]
            if _IPv4_RE.match(inner):
                parts = inner.split('.')
                if len(parts) == 4:
                    for part in parts:
                        if not part.isdigit():
                            return False
                        val = int(part)
                        if val < 0 or val > 255:
                            return False
                        if len(part) > 1 and part.startswith('0'):
                            return False
                    return True
                return False
            if _IPV6_TAG_RE.match(domain):
                return True
            return False
        return False
    domain_labels = domain.split('.')
    if len(domain_labels) < 2:
        return False
    for label in domain_labels:
        if not label:
            return False
        if len(label) > 63:
            return False
        if not _DOMAIN_LABEL_RE.match(label):
            return False
    tld = domain_labels[-1]
    if len(tld) < 2:
        return False
    if not tld.isalpha():
        return False
    return True

def validate_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    email = email.strip()
    if len(email) > EMAIL_MAX_LENGTH:
        return False
    if email.count('@') != 1:
        return False
    local_part, domain_part = email.rsplit('@', 1)
    if len(local_part) == 0 or len(local_part) > LOCAL_PART_MAX:
        return False
    if local_part.startswith('.') or local_part.endswith('.'):
        return False
    if '..' in local_part:
        return False
    if not re.match(_LOCAL_PATTERN_STR, local_part):
        return False
    if not _is_valid_domain(domain_part):
        return False
    return True
if __name__ == '__main__':
    test_emails = ['user@example.com', 'user.name+tag@example.co.uk', 'user@sub.domain.com', 'invalid@', '@invalid.com', 'user@.com', 'user@com', 'user name@example.com', 'user..name@example.com', 'user@exam..ple.com', 'a' * 64 + '@example.com', 'user@' + 'a' * 253 + '.com', 'user@[192.168.1.1]', 'user@[IPv6:2001:0db8:85a3:0000:0000:8a2e:0370:7334]', 'user@[IPv4:192.168.1.1]', 'user@192.168.1.1', '']
    results = []
    for email in test_emails:
        is_valid = validate_email(email)
        results.append((email, is_valid))
    for email, is_valid in results:
        print(f'{email!r}: {is_valid}')