def validate_email(email):
    at_count = email.count('@')
    dot_after_at = any('.' in part for part in email.split('@')[1:])
    return at_count == 1 and dot_after_at

if __name__ == '__main__':
    sample_emails = [
        "example@test.com",
        "invalid@.com",
        "@nodomain.com",
        "missingatdomain.com",
        "extra@atsign@domain.com"
    ]
    for email in sample_emails:
        print(f"{email}: {validate_email(email)}")