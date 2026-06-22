def validate_email_syntax(email):
    if not isinstance(email, str) or len(email) == 0:
        return False
    at_count = 0
    for i, char in enumerate(email):
        if char == '@':
            at_count += 1
            if at_count > 1:
                return False
            local_part = email[:i]
            domain_part = email[i+1:]
            break
    if at_count != 1:
        return False
    if not local_part or not domain_part:
        return False
    if not all(c.isalnum() or c in '._%+-' for c in local_part):
        return False
    if local_part.startswith('.') or local_part.endswith('.'):
        return False
    if '..' in local_part:
        return False
    if not domain_part or domain_part.startswith('.') or domain_part.endswith('.'):
        return False
    domain_labels = domain_part.split('.')
    if len(domain_labels) < 2:
        return False
    for label in domain_labels:
        if not label:
            return False
        if not all(c.isalnum() or c == '-' for c in label):
            return False
        if label.startswith('-') or label.endswith('-'):
            return False
    return True

if __name__ == '__main__':
    print(validate_email_syntax('test@example.com'))
    print(validate_email_syntax('invalid.email@'))
    print(validate_email_syntax('@domain.com'))
    print(validate_email_syntax('user.name+tag@domain.co.uk'))
    print(validate_email_syntax('bad..dot@domain.com'))
    print(validate_email_syntax('no-at-sign.com'))
    print(validate_email_syntax(''))
    print(validate_email_syntax('valid@sub.domain.org'))