import re

def validate_email(email: str) -> bool:
    pattern = r'^(?!(?:@[a-z]+\.))([a-zA-Z0-9._%+-]+)@(?!(?:invalid\.))([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$'
    match = re.match(pattern, email)
    return match is not None

if __name__ == '__main__':
    samples = ['test@example.com', 'user@invalid.', 'bad@@sym.com', 'valid+tag@sub.domain.org']
    results = [validate_email(s) for s in samples]
    print(results)