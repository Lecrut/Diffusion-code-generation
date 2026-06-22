import re

_email_pattern = re.compile(
    r'^(?P<local>[a-zA-Z0-9!#$%&\'*+\-/=?^_`{|}~]+)'
    r'(?P<dot>[.](?![.]))?'
    r'(?P<local_rest>[a-zA-Z0-9!#$%&\'*+\-/=?^_`{|}~]+)*'
    r'@'
    r'(?P<domain>[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?)'
    r'(?P<domain_rest>(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?)*)'
    r'\.'
    r'(?P<tld>[a-zA-Z]{2,})$'
)

def validate_email_list(emails):
    results = {}
    for email in emails:
        if not isinstance(email, str):
            results[email] = False
            continue
        if len(email) == 0:
            results[email] = False
            continue
        if email.startswith('.') or email.endswith('.'):
            results[email] = False
            continue
        if '..' in email:
            results[email] = False
            continue
        match = _email_pattern.match(email)
        results[email] = match is not None
    return results

if __name__ == '__main__':
    sample_emails = [
        "user@example.com",
        "user.name@domain.co.uk",
        "user_name@domain.com",
        "user+tag@example.org",
        "invalid.email",
        "another@invalid",
        ".startwithdot@example.com",
        "endwithdot.@example.com",
        "double..dot@example.com",
        "user@-invalid.com",
        "user@invalid-.com",
        "user@valid--domain.com",
        "valid@sub.domain.com",
        "UPPERCASE@Example.COM",
        "special!chars@domain.com",
        "quotes\"and@brackets.com",
        "",
        12345
    ]
    validation_results = validate_email_list(sample_emails)
    print(validation_results)