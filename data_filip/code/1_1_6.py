import re

def validate_email(email: str) -> bool:
    pattern = r'^(?!.*\.\.)(?!.*@@)[a-zA-Z0-9._%+-]+@(?!.*\.\.)(?!.*--)(?!.*_\.)(?!.*\._)[a-zA-Z0-9.-]+(?:\.[a-zA-Z]{2,})+$'
    if not re.match(pattern, email):
        return False
    local_part, domain_part = email.rsplit('@', 1)
    if not local_part or len(local_part) > 64:
        return False
    domain_labels = domain_part.split('.')
    if len(domain_labels) < 2:
        return False
    for label in domain_labels:
        if not label or len(label) > 63:
            return False
        if label.startswith('-') or label.endswith('-'):
            return False
        if not re.match(r'^[a-zA-Z0-9-]+$', label):
            return False
    return True

if __name__ == '__main__':
    samples = ['user@example.com', 'invalid.@domain.com', 'bad..domain@domain.com', 'valid-name+tag@sub.domain.org', 'missing@tld']
    results = [validate_email(email) for email in samples]
    print(results)