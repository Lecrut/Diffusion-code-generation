import re

def validate_email(email):
    pattern = r'^(?=.*[a-zA-Z0-9._%+-])[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    domain_pattern = r'^(?=.*[a-zA-Z])a-zA-Z0-9.-+\.(?=.*[a-zA-Z])a-zA-Z]{2,}'
    if not re.match(pattern, email):
        return False
    domain_part = email.split('@', 1)[1]
    if not re.match(domain_pattern, domain_part):
        return False
    return True

if __name__ == '__main__':
    sample_emails = [
        "user@example.com",
        "invalid.email@domain",
        "good.name+tag@sub.domain.org",
        "another@valid-domain.co.uk",
        "no-at-sign.com",
        "@missinglocal.com",
        "missing@domain"
    ]
    for email in sample_emails:
        print(validate_email(email))