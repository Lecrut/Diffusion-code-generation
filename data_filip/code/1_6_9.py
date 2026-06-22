import re

email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

def validate_email(email):
    return bool(email_pattern.match(email))

if __name__ == '__main__':
    test_emails = [
        "user@example.com",
        "john.doe+tag@company.co.uk",
        "invalid@",
        "@invalid.com",
        "user@.com",
        "user@com",
        "spaces in@email.com",
        "user@domain..com",
        "simple@example.org",
        "x@y.zz"
    ]
    results = {email: validate_email(email) for email in test_emails}
    print(results)