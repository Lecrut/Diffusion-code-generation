import re

def validate_email(email):
    pattern = r'^(?!.*@.*@)(?!.*\.\.)(?![.])(?!.*\.$)[a-zA-Z0-9._%+-]+@(?!.*[.][.])[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

if __name__ == '__main__':
    sample_emails = [
        "user@example.com",
        "invalid@.com",
        "test@domain.co.uk",
        "@missinguser.com",
        "user@com",
        "valid.email+tag@sub.domain.org",
        "bad@@double.com",
        "spaces@in email.com",
        "trailing.dot.@domain.",
        "a@b.c",
        "user@domain..com"
    ]
    results = [validate_email(email) for email in sample_emails]
    for email, valid in zip(sample_emails, results):
        print(valid)