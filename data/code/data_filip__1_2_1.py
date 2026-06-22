import re

_DOMAIN_RE = re.compile(r'^[a-zA-Z0-9]([a-zA-Z0-9\-]*[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9\-]*[a-zA-Z0-9])?)*$')

def validate_email(email: str) -> bool:
    if not isinstance(email, str) or '@' not in email:
        return False
    
    parts = email.split('@')
    if len(parts) != 2:
        return False
    
    local_part, domain_part = parts
    
    if not local_part or not domain_part:
        return False
    
    for char in local_part:
        if not (char.isalnum() or char in '.-_+'):
            return False
        if char == '.' and (local_part.startswith('.') or local_part.endswith('.') or '..' in local_part):
            return False
    
    if not _DOMAIN_RE.match(domain_part):
        return False
    
    if '..' in domain_part or domain_part.startswith('-') or domain_part.endswith('-'):
        return False
    
    return True

if __name__ == '__main__':
    print(validate_email("user@example.com"))
    print(validate_email("invalid-email.com"))
    print(validate_email("user@.com"))
    print(validate_email("user@com"))
    print(validate_email("user.name@sub.domain.com"))
    print(validate_email("@domain.com"))
    print(validate_email("user@"))
    print(validate_email(""))