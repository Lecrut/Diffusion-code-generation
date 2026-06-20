import re

def is_valid_email(email: str) -> bool:
    pattern = '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, email):
        return True
    else:
        return False
if __name__ == '__main__':
    sample_emails = ['test@example.com', 'invalid-email@', 'another.test+tag@domain.co.uk', '@missing-local.com', 'no-at-sign.com', 'spaces in@email.com', 'valid123@domain.museum', 'under_score@domain-name.com', 'special!char@domain.com', 'multiple..dots@domain.com']
    for email in sample_emails:
        result = is_valid_email(email)
        print(f'{email}: {result}')