import re
import string

def validate_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    
    length = len(email)
    if length < 3 or length > 254:
        return False
    
    if email[0] == '.' or email[-1] == '.':
        return False
    
    if '..' in email:
        return False
    
    at_index = email.rfind('@')
    if at_index == -1:
        return False
    
    local_part = email[:at_index]
    domain_part = email[at_index + 1:]
    
    if not local_part or not domain_part:
        return False
    
    if len(local_part) > 64:
        return False
    
    allowed_special_chars = "!#$%&'*+/=?^_`{|}~.-"
    for char in local_part:
        if char.isalnum() or char in allowed_special_chars:
            continue
        if char == '.':
            prev_idx = local_part.index(char)
            if prev_idx == 0 or local_part[prev_idx - 1] != '.':
                continue
        return False
    
    domain_labels = domain_part.split('.')
    if len(domain_labels) < 2:
        return False
    
    for label in domain_labels:
        if not label:
            return False
        if len(label) > 63:
            return False
        if label[0] == '-' or label[-1] == '-':
            return False
        for char in label:
            if not (char.isalnum() or char == '-'):
                return False
    
    try:
        domain_part.encode('ascii')
        local_part.encode('ascii')
    except UnicodeEncodeError:
        return False
    
    if domain_part.count('.') == 0:
        return False
    
    pattern = r'^(?!\.)((?:[a-zA-Z0-9!#$%&\'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&\'*+/=?^_`{|}~-]+)*|"((?:[ \t]|[^"\\])|\\.)*")\.)+(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?|[\u0080-\uFFFF])$'
    
    return bool(re.match(pattern, email, re.IGNORECASE))

if __name__ == '__main__':
    test_cases = [
        "user@example.com",
        "user.name+tag@example.co.uk",
        "user@sub.example.com",
        "user@-invalid.com",
        "user.@example.com",
        ".user@example.com",
        "user@.com",
        "user@example",
        "user name@example.com",
        "user@@example.com",
        "user@exam ple.com",
        "plainaddress",
        "@missing-local.com",
        "user@example..com",
        "user@192.168.1.1",
        "long" + "a" * 60 + "@example.com",
        "user@ex" + "a" * 63 + "mple.com",
        "user@example.c",
        "user@example.com.",
        "user@ex_ample.com",
        'user"test"@example.com'
    ]
    
    for email in test_cases:
        result = validate_email(email)
        print(f"{email}: {result}")