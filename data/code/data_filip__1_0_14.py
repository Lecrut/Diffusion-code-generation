import re

EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

def validate_emails(email_list):
    results = []
    for email in email_list:
        if EMAIL_PATTERN.match(email):
            results.append(True)
        else:
            results.append(False)
    return results

if __name__ == '__main__':
    test_emails = [
        "user@example.com",
        "user.name+tag@sub.domain.co",
        "invalid-email@",
        "@missing-local.com",
        "no-domain",
        "special!char@test.com",
        "valid_user-123@domain-name.org"
    ]
    print(validate_emails(test_emails))