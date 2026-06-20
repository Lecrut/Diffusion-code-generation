import re

def validate_email(email):
    pattern = r'^(?!.*\.\.)[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+(\.[a-zA-Z]{2,})+$'
    lookahead_pattern = r'^(?=.*[a-zA-Z0-9])(?!.*\.\.)'
    domain_pattern = r'^[a-zA-Z0-9._%+-]+@'
    
    if not re.search(lookahead_pattern, email):
        return False
    if not re.match(domain_pattern, email):
        return False
    
    full_match = re.match(pattern, email)
    return bool(full_match)

if __name__ == '__main__':
    samples = [
        "user@example.com",
        "user..name@example.com",
        "invalid-email@",
        "another@valid-domain.org",
        "no-at-sign.com",
        "bad@.com",
        "good.name+tag@sub.domain.co"
    ]
    for s in samples:
        result = validate_email(s)
        print(result)