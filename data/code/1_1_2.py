import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        domain = email.split('@')[1]
        if len(domain.split('.')) >= 2 and len(domain.split('.')[-1]) >= 2:
            return True
        return False
    return False

if __name__ == '__main__':
    sample_emails = ['test@example.com', 'invalid.email', 'user@domain.org', 'bad@.com', 'good@sub.domain.co.uk']
    for email in sample_emails:
        print(validate_email(email))