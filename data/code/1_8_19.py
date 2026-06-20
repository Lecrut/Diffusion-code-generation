import re

def validate_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    
    if len(email) > 254:
        return False
    
    at_count = email.count('@')
    if at_count != 1:
        return False
    
    local_part, domain_part = email.split('@')
    
    if len(local_part) == 0 or len(local_part) > 64:
        return False
    
    if len(domain_part) == 0:
        return False
    
    if domain_part[0] == '.' or domain_part[-1] == '.':
        return False
    
    if '..' in domain_part:
        return False
    
    domain_labels = domain_part.split('.')
    for label in domain_labels:
        if len(label) == 0:
            return False
        if len(label) > 63:
            return False
        if label[0] == '-' or label[-1] == '-':
            return False
    
    local_pattern = r"^[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)*$"
    domain_label_pattern = r"^[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?$"
    
    if not re.match(local_pattern, local_part):
        return False
    
    for label in domain_labels:
        if not re.match(domain_label_pattern, label):
            return False
    
    if len(domain_labels) < 2:
        return False
    
    tld = domain_labels[-1]
    if not re.match(r'^[a-zA-Z][a-zA-Z0-9]*$', tld):
        return False
    if len(tld) < 2:
        return False
    
    return True

if __name__ == '__main__':
    test_cases = [
        "user@example.com",
        "invalid@",
        "@missing.com",
        "user@.com",
        "user@com.",
        "user name@example.com",
        "user..dot@example.com",
        "user@-example.com",
        "user@example-.com",
        "user@example.c",
        "a@b.co",
        "user@localhost",
        "",
        "user@exam_ple.com",
        "very.long.local.part@very.long.domain.part.com",
        "user@example..com",
        "user@example.COM",
        "user@123.123.123.123",
        "invalid@@example.com",
        "user@exam ple.com"
    ]
    
    for case in test_cases:
        result = validate_email(case)
        print(f"validate_email({case!r}) -> {result}")