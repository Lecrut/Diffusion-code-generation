import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

if __name__ == '__main__':
    test_cases = ['user@example.com', 'invalid.email@', 'no-at-symbol.com', 'valid.user@domain.org', '@domain.com', 'user@domain']
    for case in test_cases:
        print(is_valid_email(case))