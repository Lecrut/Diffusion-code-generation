def capitalize_first_letter(s):
    if not s:
        return s
    return s[0].upper() + s[1:]

if __name__ == '__main__':
    result1 = capitalize_first_letter('hello')
    print(result1)

    result2 = capitalize_first_letter('')
    print(result2)

    result3 = capitalize_first_letter('a')
    print(result3)

    result4 = capitalize_first_letter('already Capitalized')
    print(result4)

    result5 = capitalize_first_letter('123abc')
    print(result5)

    assert result1 == 'Hello'
    assert result2 == ''
    assert result3 == 'A'
    assert result4 == 'Already Capitalized'
    assert result5 == '123abc'