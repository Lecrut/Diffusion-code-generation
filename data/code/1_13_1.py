import re

def validate_emails(email_list):
    pattern = re.compile(
        r'^(?P<name>[a-zA-Z0-9._%+-]+)'
        r'@'
        r'(?P<domain>[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$'
    )
    results = []
    for email in email_list:
        if pattern.match(email):
            results.append(True)
        else:
            results.append(False)
    return results

if __name__ == '__main__':
    sample_emails = [
        "user@example.com",
        "user.name+tag@domain.co.uk",
        "invalid-email@",
        "@missing-local.com",
        "no-at-sign.com",
        "valid@sub.domain.org",
        "spaces in@email.com",
        "double@@at.com",
        "trailing.@domain.com",
        "valid123@test-domain.net"
    ]
    print(validate_emails(sample_emails))