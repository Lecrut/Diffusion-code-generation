def capitalize_first_letter(s):
    if not s:
        return s
    return s[0].upper() + s[1:]

if __name__ == '__main__':
    assert capitalize_first_letter('') == ''
    assert capitalize_first_letter('a') == 'A'
    assert capitalize_first_letter('hello') == 'Hello'
    assert capitalize_first_letter('Hello') == 'Hello'
    assert capitalize_first_letter('HELLO') == 'HELLO'
    assert capitalize_first_letter('hELLO') == 'HELLO'
    assert capitalize_first_letter('  hello') == '  hello'
    print(capitalize_first_letter('hello'))
    print(capitalize_first_letter(''))
    print(capitalize_first_letter('world'))