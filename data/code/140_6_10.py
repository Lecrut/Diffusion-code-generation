def validate_email(email):
    at_count = email.count('@')
    dot_after_at = any(('.' in part for part in email.split('@')[1:] if '@' not in part))
    return at_count == 1 and dot_after_at
if __name__ == '__main__':
    print(validate_email('example@test.com'))
    print(validate_email('example.test@com'))
    print(validate_email('example@test.co.uk'))
    print(validate_email('example@test.'))
    print(validate_email('@test.com'))
    print(validate_email('example@test'))