import re

def is_valid_email(email):
    if not isinstance(email, str):
        return False
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

if __name__ == '__main__':
    sample_emails = ["user@example.com", "invalid.email@", "test@domain", "admin@site.co.uk", "no_at_symbol.com"]
    for email in sample_emails:
        print(is_valid_email(email))