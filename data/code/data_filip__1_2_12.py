import re

DOMAIN_REGEX = re.compile(r'^[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)+$')

def validate_email(email):
    if not isinstance(email, str) or '@' not in email:
        return False
    
    parts = email.split('@')
    if len(parts) != 2:
        return False
    
    local_part, domain_part = parts
    
    if not local_part or not domain_part:
        return False
    
    if len(local_part) > 64 or len(domain_part) > 253:
        return False
    
    allowed_local_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.!#$%&\'*+/=?^_`{|}~-')
    if not all(char in allowed_local_chars for char in local_part):
        return False
    
    if local_part.startswith('.') or local_part.endswith('.'):
        return False
    
    if '..' in local_part:
        return False
    
    if not DOMAIN_REGEX.match(domain_part):
        return False
    
    return True

if __name__ == '__main__':
    test_emails = [
        "user@example.com",
        "invalid.email",
        "@example.com",
        "user@",
        "user@.com",
        "user@com",
        "user name@example.com",
        "user@exam ple.com",
        "valid.email+tag@sub.domain.org",
        "a@b.co",
        "",
        "user@localhost",
        "user@-domain.com",
        "user@domain-.com",
        ".user@example.com",
        "user.@example.com",
        "us..er@example.com"
    ]
    
    for email in test_emails:
        print(validate_email(email))