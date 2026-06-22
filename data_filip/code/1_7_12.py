import re

def is_valid_email(email):
    if not isinstance(email, str):
        return False
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

if __name__ == '__main__':
    sample_emails = ['user@example.com', 'invalid-email@', '@domain.com', 'valid.user@sub.domain.org']
    results = [is_valid_email(email) for email in sample_emails]
    print(results)