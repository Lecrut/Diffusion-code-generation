import re

LOCAL_PART_PATTERN = r"[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+"
DOMAIN_PART_PATTERN = r"[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*\.[a-zA-Z]{2,}"
COMPILED_EMAIL_PATTERN = re.compile(rf"^{LOCAL_PART_PATTERN}@{DOMAIN_PART_PATTERN}$")

def parse_and_validate(email_address):
    if not isinstance(email_address, str):
        return False
    if not email_address or "@" not in email_address:
        return False
    
    match = COMPILED_EMAIL_PATTERN.match(email_address)
    if not match:
        return False
    
    parts = email_address.split("@")
    if len(parts) != 2:
        return False
    
    local_part, domain = parts
    
    if not local_part:
        return False
    
    if local_part.startswith(".") or local_part.endswith("."):
        return False
    
    if ".." in local_part:
        return False
    
    if not domain or domain.startswith(".") or domain.endswith("."):
        return False
    
    return True

if __name__ == '__main__':
    test_cases = [
        "alice.smith@example.com",
        "bob+newsletter@sub.domain.org",
        "charlie@test.co",
        ".invalid@start.com",
        "double..dot@domain.com",
        "spaces fail@domain.com",
        "no-at-sign.com",
        "trailing.dot.@domain.com"
    ]
    
    validation_results = []
    for test_email in test_cases:
        is_valid = parse_and_validate(test_email)
        validation_results.append(is_valid)
    
    print(validation_results)