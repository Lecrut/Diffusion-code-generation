def validate_email(email):
    at_count = email.count('@')
    dot_after_at = any('.' in part for part in email.split('@')[1:])
    return at_count == 1 and dot_after_at

if __name__ == '__main__':
    sample_email = 'example@test.com'
    print(validate_email(sample_email))