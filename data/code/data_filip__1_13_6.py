import re

def validate_email_list(email_list):
    pattern = re.compile(
        r'^(?P<local>[a-zA-Z0-9_.+-]+)'
        r'@'
        r'(?P<domain>[a-zA-Z0-9-]+)'
        r'(\.(?P<subdomain>[a-zA-Z0-9-]+))*'
        r'\.(?P<tld>[a-zA-Z]{2,})$'
    )
    results = []
    for email in email_list:
        if not isinstance(email, str):
            results.append(False)
            continue
        results.append(bool(pattern.match(email)))
    return results

if __name__ == '__main__':
    sample_emails = [
        "user@example.com",
        "user.name+tag@sub.domain.co.uk",
        "invalid-email@",
        "@missinglocal.com",
        "no-at-symbol.com",
        "spaces in@email.com",
        "valid@domain.io",
        "another_valid.user123@test-domain.org"
    ]
    print(validate_email_list(sample_emails))