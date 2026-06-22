import re

def validate_email_rfc5322(email):
    atext = r'[A-Za-z0-9!#$%&\'*+\-/=?^_`{|}~]'
    dot_atom_text = r'(?:' + atext + r'+\.)*' + atext + r'+'
    dtext = r'[A-Za-z0-9!#$%&\'*+\-/=?^_`{|}~\x21\x23-\x27\x2A\x2B\x2D\x2E\x2F\x3A-\x3E\x3F\x5B-\x5E\x60\x7B-\x7E]'
    quoted_pair = r'\\[\x00-\x7F]'
    quoted_string = r'"(?:' + quoted_pair + r'|[^"\\])*"'
    local_part_dot_atom = dot_atom_text
    local_part_quoted = quoted_string
    local_part = r'(?:' + local_part_dot_atom + r'|' + local_part_quoted + r')'
    domain_literal_content = r'(?:' + dtext + r'|' + quoted_pair + r')*'
    domain_literal = r'\[' + domain_literal_content + r'\]'
    domain = r'(?:' + dot_atom_text + r'|' + domain_literal + r')'
    pattern = r'^' + local_part + r'@' + domain + r'$'
    return bool(re.match(pattern, email))

if __name__ == '__main__':
    test_cases = [
        'simple@example.com',
        'very.common@example.com',
        'disposable.style.email.with+symbol@example.com',
        'other.email-with-hyphen@example.com',
        'fully-qualified-domain@example.com',
        'user.name+tag+sorting@example.com',
        'x@example.com',
        'example-indeed@strange-example.com',
        'test/test@test.com',
        'postmaster@example.com',
        'user@[IPv6:2001:db8:1ff::a0b:dbd0]',
        '"very.unusual.@.com"@example.com',
        '"very.unusual.@.com"@example.com',
        'a@b',
        'invalid@example',
        '@missing-local.com',
        'missing-at-sign.com',
        'two@at@signs.com',
        ' spaces@example.com',
        'space@in .com',
        'user@[192.168.1.1]',
        'invalid..double@dot.com',
        'user.name..with..dots@example.com',
        "user\\\"name@example.com",
        'user\\@name@example.com',
        'ab@cy',
        'a@b.c',
        '12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890@example.com',
        'short@example.com',
        'a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.x.y.z@example.com',
        '123.123.123.123@example.com',
        'user_name@example.com',
        'user-name@example.com',
        'user=name@example.com',
        'user+name@example.com',
        'user!name@example.com',
        'user#name@example.com',
        'user$name@example.com',
        'user%name@example.com',
        'user&name@example.com',
        'user\'name@example.com',
        'user*name@example.com',
        'user+name@example.com',
        'user-name@example.com',
        'user.name@example.com',
        'user_name@example.com',
        'user=name@example.com',
        'user?name@example.com',
        'user^name@example.com',
        'user`name@example.com',
        'user{name@example.com',
        'user}name@example.com',
        'user|name@example.com',
        'user~name@example.com',
        'user[name@example.com',
        'user]name@example.com',
        'user\\name@example.com',
        'user"name@example.com',
        'user:name@example.com',
        'user;name@example.com',
        'user<name@example.com',
        'user>name@example.com',
        'user,name@example.com',
        'user/name@example.com'
    ]
    for email in test_cases:
        print(f"{email}: {validate_email_rfc5322(email)}")