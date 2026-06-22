import re

RFC5322_EMAIL_RE = re.compile(
    r"""
    ^
    (?:
        # Quoted string local-part
        "(?:[^"\\]|\\.)*"
        # Or dot-atom local-part
        | [a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)*
    )
    @
    (?:
        # Domain: dot-atom
        [a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?
        (?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?)*
        # Or domain-literal
        | \[
            (?:
                [^\]\\\\]
                | \\.
            )
        \]
    )
    $
    """,
    re.VERBOSE
)

def validate_email_rfc5322(email: str) -> bool:
    if not isinstance(email, str):
        return False
    return bool(RFC5322_EMAIL_RE.match(email))

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
        "john.doe@johns-domain.com",
        "mailhost!username@example.org",
        "user%example.com@example.org",
        "postmaster@example.org",
        "jsmith@example.com",
        "user@localhost",
        "user@[IPv6:2001:db8::1]",
        "invalid@example",
        "@example.com",
        "user@.com",
        "user@com.",
        "",
        "user name@example.com",
        "user@com..com"
    ]
    for s in samples:
        print(f"{s}: {validate_email_rfc5322(s)}")