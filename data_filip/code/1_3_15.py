import re

def validate_email_rfc5322(email):
    local_part_pattern = r'(?:(?:[a-zA-Z0-9!#$%&\'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&\'*+/=?^_`{|}~-]+)*)|"(?:[\x01-\x08\x0B\x0C\x0E-\x1F\x21\x23-\x5B\x5D-\x7E]|\\[\x01-\x09\x0B\x0C\x0E-\x7F])*")'
    domain_pattern = r'(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?)*)'
    full_pattern = f'^{local_part_pattern}@{domain_pattern}$'
    return bool(re.match(full_pattern, email))

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
        "mailhost!username@example.org",
        "user%example.com@example.org",
        "user-@example.org",
        "postmaster@ipv4.127.0.0.1",
        "user@[IPv6:2001:db8:1ff::a0b:dbd0]",
        "Abc.example.com",
        "A@b.cd",
        "!def!xyz%abc@example.com",
        "1234567890@example.com",
        "email@example.com",
        "firstname.lastname@example.com",
        "email@subdomain.example.com",
        "firstname+lastname@example.com",
        "email@123.123.123.123",
        "1234567890@domain.com",
        "_______@domain.com",
        "email@domain-one.com",
        "email@domain.name",
        "email@domain.co.jp",
        "firstname-lastname@example.com",
        "much." + "needed@example.com",
        "mails@mail.com",
        "test/test@test.com",
        "test@test.com",
        "test@com.com",
        "a@b.c",
        "a@b.co",
        "very.unusual.@.unusual.com@example.com",
        "a..b@c..com",
        "plainaddress",
        "some@",
        "@missing-local.com",
        "missing-local@",
        "invalid@.com",
        "invalid@com.",
        "invalid@@double.com",
        "@@.com",
        "",
        " "
    ]
    for sample in samples:
        result = validate_email_rfc5322(sample)
        print(f"{sample}: {result}")