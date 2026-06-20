def validate_email_syntax(email):
    if not isinstance(email, str) or len(email) == 0:
        return False
    at_count = 0
    dot_count_in_domain = 0
    local_end = -1
    for i, char in enumerate(email):
        if char == '@':
            at_count += 1
            if at_count > 1:
                return False
            local_end = i
        elif char == '.' and i != local_end - 1 and i > local_end:
            dot_count_in_domain += 1
    if at_count != 1:
        return False
    if local_end == 0 or local_end == len(email) - 1:
        return False
    local_part = email[:local_end]
    domain_part = email[local_end + 1:]
    if not local_part or not domain_part:
        return False
    allowed_local = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.!#$%&\'*+/=?^_`{|}~-')
    for char in local_part:
        if char not in allowed_local:
            return False
    if not (domain_part[0].isalpha() or domain_part[0].isdigit()):
        return False
    if not (domain_part[-1].isalpha() or domain_part[-1].isdigit()):
        return False
    if '.' not in domain_part:
        return False
    labels = domain_part.split('.')
    if any(not label for label in labels):
        return False
    for label in labels:
        if not (label[0].isalpha() or label[0].isdigit()):
            return False
        if not (label[-1].isalpha() or label[-1].isdigit()):
            return False
        for char in label:
            if not (char.isalpha() or char.isdigit() or char == '-'):
                return False
    return True

if __name__ == '__main__':
    print(validate_email_syntax("user@example.com"))
    print(validate_email_syntax("invalid-email"))
    print(validate_email_syntax("user@.com"))
    print(validate_email_syntax("@example.com"))
    print(validate_email_syntax("user@com"))