def validate_email(email):
    at_count = email.count('@')
    dot_count_after_at = email.split('@', 1)[1].count('.') if '@' in email else 0
    return at_count == 1 and dot_count_after_at >= 1

if __name__ == '__main__':
    sample_email = 'example@test.com'
    print(validate_email(sample_email))