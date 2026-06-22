import re

_LOCAL_ATOM_CHAR = r"[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]"
_DOT_ATOM = r"(?:" + _LOCAL_ATOM_CHAR + r"+\.)*" + _LOCAL_ATOM_CHAR + r"+"
_QUOTED_PAIR = r"\\[\x00-\x7F]"
_QUOTED_STRING = r'"(?:' + _QUOTED_PAIR + r'|[^"\\])*"'
_LOCAL_PART = r"(?:" + _DOT_ATOM + r"|" + _QUOTED_STRING + r")"
_DTEXT = r"[A-Za-z0-9!#$%&'*+/=?^_`{|}~\x21\x23-\x27\x2A\x2B\x2D\x2E\x2F\x3A-\x3E\x3F\x5B-\x5E\x60\x7B-\x7E]"
_DOMAIN_LITERAL = r"\[(?:" + _DTEXT + r"|" + _QUOTED_PAIR + r")*\]"
_DOMAIN = r"(?:" + _DOT_ATOM + r"|" + _DOMAIN_LITERAL + r")"
_RFC5322_PATTERN = re.compile(r"^" + _LOCAL_PART + r"@" + _DOMAIN + r"$")

def validate_email_rfc5322(address):
    return bool(_RFC5322_PATTERN.match(address))

if __name__ == '__main__':
    samples = [
        "simple@example.com",
        "very.common@example.org",
        "disposable.style.email.with+symbol@example.com",
        "other.email-with-hyphen@example.com",
        "fully-qualified-domain@example.com",
        "user.name+tag+sorting@example.com",
        "x@example.com",
        "example-indeed@strange-example.com",
        "test/test@test.com",
        "mailhost!username@example.org",
        "user%example.com@example.org",
        "postmaster@[IPv6:2001:DB8::1]",
        "not an email",
        "user@.com",
        "@missing-local.com",
        "",
        "a" * 64 + "@example.com",
        "user@[127.0.0.1]",
        '"quoted"@example.com',
        'user name@example.com'
    ]
    for sample in samples:
        print(validate_email_rfc5322(sample))