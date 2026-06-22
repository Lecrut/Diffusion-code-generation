import re

def validate_email_rfc5322(email):
    atext = r'[A-Za-z0-9!#$%&\'*\+/=?^_`{|}~-]'
    dot_atom_text = atext + r'(' + r'\.' + atext + r'+)*'
    domain_literal_inner = r'[^\x00-\x08\x0A-\x1F\x7F\\"\\\\]*'
    quoted_pair = r'\\\\[\\x00-\\x7F]'
    dtext = r'[\\x21-\\x5A\\x5E-\\x7E]'
    domain_literal = r'\\[' + r'(?:' + quoted_pair + r'|' + dtext + r')*' + r'\\]'
    domain = r'(?:' + dot_atom_text + r'|' + domain_literal + r')'
    dot_atom = r'(?:' + atext + r'+(?:\.' + atext + r'+)*' + r')'
    qcontent = r'(?:' + quoted_pair + r'|[\\x21\\x23-\\x5B\\x5D-\\x7E])'
    quoted_string = r'"(?:' + qcontent + r')*"'
    local_part = r'(?:' + dot_atom + r'|' + quoted_string + r')'
    pattern = r'^' + local_part + r'@' + domain + r'$'
    return bool(re.match(pattern, email, re.IGNORECASE))

if __name__ == '__main__':
    samples = [
        "simple@example.com",
        "very.common@example.com",
        "disposable.style.email.with+symbol@example.com",
        "other.email-with-hyphen@example.com",
        "fully-qualified-domain@example.com",
        "user.name+tag+sorting@example.com",
        "x@example.com",
        "example-indeed@strange-example.com",
        "test/test@test.com",
        "john..doe@example.com",
        "@missing-local.com",
        "missing-at-sign.com",
        "spaces in local@part.com",
        "trailing.dot.@example.com",
        "leading.dot@example.com",
        "a.b@c.d",
        "name/surname@example.com",
        "very.(),:;<>[]\".VERY.\"very@\\ \"very\".unusual@strange.example.com",
        "admin@mailserver1",
        "user%example.com@example.org"
    ]
    for s in samples:
        print(validate_email_rfc5322(s))