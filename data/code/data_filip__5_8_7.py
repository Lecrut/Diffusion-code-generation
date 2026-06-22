def capitalize_first_letter(s: str) -> str:
    if not s:
        return s
    return s[0].upper() + s[1:]

if __name__ == '__main__':
    assert capitalize_first_letter('') == ''
    assert capitalize_first_letter('hello') == 'Hello'
    assert capitalize_first_letter('HELLO') == 'HELLO'
    assert capitalize_first_letter('h') == 'H'
    assert capitalize_first_letter('hello world') == 'Hello world'

    result = capitalize_first_letter('example string')
    print(result)