import re

def validate_email_rfc5322(email):
    atext = r'[A-Za-z0-9!#$%&\'*+\-/=?^_`{|}~]'
    dot_atom_text = r'(?:' + atext + r'+\.)+' + atext + r'+'
    quoted_string = r'"(?:[^"\\]|\\.)*"'
    local_part = r'(?:' + dot_atom_text + r'|' + quoted_string + r')'
    domain_literal = r'\[+(?:[^\\\]]|\\.)*\]+[A-Za-z0-9\-\._~]'
    domain_literal_pattern = r'\[+(?:[^\\\]]|\\.)*\]+'
    domain = r'(?:' + dot_atom_text + r'|' + domain_literal_pattern + r')'
    pattern = r'^' + local_part + r'@' + domain + r'$'
    return bool(re.match(pattern, email))

if __name__ == '__main__':
    sample_emails = [
        "user@example.com",
        "first.last@example.co.uk",
        "user123+tag@example.org",
        '"quoted name"@example.com',
        "invalid@.com",
        "@missing-local.com",
        "no-at-sign.com",
        "user@.invalid",
        "plainaddress",
        "user@com",
        "john.doe@example",
        "simple@example",
        '"very.unusual.@.unusual.com"@example.com',
        "unusual.\\@.unusual@example.com",
        "a@b",
        "Abc@example.com",
        "Abc.def@example.com",
        "user%example.com@example.com"
    ]
    for email in sample_emails:
        result = validate_email_rfc5322(email)
        print(f"{email}: {result}")