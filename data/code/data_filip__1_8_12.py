import re
import string

MAX_EMAIL_LENGTH = 254
MAX_LOCAL_LENGTH = 64
MAX_DOMAIN_LENGTH = 253
MAX_LABEL_LENGTH = 63

ALLOWED_LOCAL_CHARS = frozenset(
    string.ascii_letters + string.digits + "!#$%&'*+/=?^_`{|}~-"
)

LOCAL_QUOTED_PATTERN = re.compile(r'^"[^"]*"$')
LOCAL_UNQUOTED_PATTERN = re.compile(r'^[a-zA-Z0-9!#$%&\'*+/=?^_`{|}~-]+$')

DOMAIN_LABEL_PATTERN = re.compile(r'^[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?$')
DOMAIN_IP_PATTERN = re.compile(r'^\[(IPv4|IPv6):.+\]$')

def _validate_local_part(local: str) -> bool:
    if not local:
        return False
    if len(local) > MAX_LOCAL_LENGTH:
        return False
    
    if local.startswith('"'):
        if not LOCAL_QUOTED_PATTERN.match(local):
            return False
        content = local[1:-1]
        if not content:
            return False
        if '"' in content or '\\' in content:
            if '"' in content:
                return False
        return True
    
    if local.startswith('.') or local.endswith('.'):
        return False
    if '..' in local:
        return False
    
    for char in local:
        if char not in ALLOWED_LOCAL_CHARS:
            return False
    
    if local.endswith('.'):
        return False
        
    return True

def _validate_domain_part(domain: str) -> bool:
    if not domain:
        return False
    if len(domain) > MAX_DOMAIN_LENGTH:
        return False
    
    if domain.startswith('['):
        return DOMAIN_IP_PATTERN.match(domain) is not None
    
    if domain.endswith('.') or domain.startswith('.'):
        return False
    if '..' in domain:
        return False
    
    labels = domain.split('.')
    if not labels:
        return False
    
    if len(labels) < 2:
        return False
    
    if not labels[-1].isalpha():
        return False
        
    for label in labels:
        if not label:
            return False
        if len(label) > MAX_LABEL_LENGTH:
            return False
        if label.startswith('-') or label.endswith('-'):
            return False
        if not DOMAIN_LABEL_PATTERN.match(label):
            return False
            
    return True

class EmailValidator:
    def __init__(self):
        self._local_pattern = LOCAL_UNQUOTED_PATTERN
    
    def validate(self, email: str) -> bool:
        if not isinstance(email, str):
            return False
        
        email = email.strip()
        
        if len(email) > MAX_EMAIL_LENGTH:
            return False
        
        if email.count('@') != 1:
            return False
        
        local_part, domain_part = email.split('@', 1)
        
        if not _validate_local_part(local_part):
            return False
        
        if not _validate_domain_part(domain_part):
            return False
        
        return True

if __name__ == '__main__':
    validator = EmailValidator()
    test_cases = [
        "user@example.com",
        "user.name+tag@sub.domain.co.uk",
        "invalid@.com",
        "too_long_" + "a" * 70 + "@example.com",
        "user@invalid-domain",
        '"quoted"user@domain.com',
        "simple@test.org",
        "no-at-sign.com",
        "@missing-local.com",
        "missing-domain@",
        "double@@at.com",
        "trailing.@domain.com",
        "valid@192.168.1.1"
    ]
    
    for case in test_cases:
        result = validator.validate(case)
        print(f"{case}: {result}")