import re

def validate_email_rfc5322(email):
    atext = r'[A-Za-z0-9!\#$%&\'*+\-/=?^_`{|}~]'
    dot_atom_text = r'(?:' + atext + r'+\.)+' + atext + r'+'
    dot_atom = r'(?:' + dot_atom_text + r')'
    quoted_pair = r'\\[\x00-\x7F]'
    qtext = r'[\x21\x23-\x5B\x5D-\x7E]'
    quoted_string = r'"(?:' + quoted_pair + r'|' + qtext + r')*"'
    obs_local_part_chars = r'[A-Za-z0-9!#$%&\'*+\-/=?^_`{|}~]'
    obs_local_part = r'(?:' + obs_local_part_chars + r'\.)+' + obs_local_part_chars + r'+'
    local_part = r'(?:' + dot_atom + r'|' + quoted_string + r'|' + obs_local_part + r')'
    domain_literal_inner = r'(?:\\[\x00-\x7E]|[\x21-\x5A\x5E-\x7E])'
    domain_literal = r'\[(?:' + domain_literal_inner + r')*\]'
    domain = r'(?:' + dot_atom + r'|' + domain_literal + r')'
    address = r'^' + local_part + r'@' + domain + r'$'
    pattern = re.compile(address, re.IGNORECASE)
    return bool(pattern.match(email))

if __name__ == '__main__':
    valid_emails = [
        "simple@example.com",
        "very.common@example.com",
        "disposable.style.email.with+symbol@example.com",
        "other.email-with-hyphen@example.com",
        "fully-qualified-domain@example.com",
        "user.name+tag+sorting@example.com",
        "x@example.com",
        "example-indeed@strange-example.com",
        "test/test@test.com",
        '"john..doe"@example.org',
        "mailhost!username@example.org",
        "user%example.com@example.org",
        "user-@example.org",
        "postmaster@example.org",
        "John.Doe@example.com",
        'john.doe+john.doe@example.com',
        "test123@example.com",
        "email@example.co.jp",
        "firstname-lastname@example.com",
        "name/surname@example.com",
        "x@example.com",
        "test/test@test.com",
        '" "@example.org',
        '"john.doe"@example.org',
        'mailhost!username@example.org',
        "user%example.com@example.org",
        "user-@example.org",
        "postmaster@example.org",
        "John.Doe@example.com",
        'john.doe+john.doe@example.com',
        "test123@example.com",
        "email@example.co.jp",
        "firstname-lastname@example.com",
        "name/surname@example.com",
    ]
    invalid_emails = [
        "plainaddress",
        "@missingusername.com",
        "username@.com",
        "username@com",
        "username@.com.",
        ".username@example.com",
        "username..username@example.com",
        "username@.example.com",
        "username@example..com",
        "Abc.example.com",
        "A@b@c@example.com",
        "justin@example",
        "",
        " ",
        "user@exam ple.com",
        "user@.com",
        "user@com.",
        "user@..com",
        "user@com",
        "user@",
        "@example.com",
        "user@example",
        "a]b[c@example.com",
        "user@[123.123.123",
    ]
    results = []
    for email in valid_emails:
        results.append(validate_email_rfc5322(email))
    for email in invalid_emails:
        results.append(not validate_email_rfc5322(email))
    print(all(results))