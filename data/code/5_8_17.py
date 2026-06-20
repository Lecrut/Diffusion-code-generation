def capitalize_first(s):
    if not s:
        return s
    return s[0].upper() + s[1:]

if __name__ == '__main__':
    result1 = capitalize_first('hello')
    print(result1)
    result2 = capitalize_first('world')
    print(result2)
    result3 = capitalize_first('')
    print(result3)
    result4 = capitalize_first('a')
    print(result4)
    result5 = capitalize_first('alreadyCapitalized')
    print(result5)
    result6 = capitalize_first('123abc')
    print(result6)

    assert capitalize_first('hello') == 'Hello'
    assert capitalize_first('world') == 'World'
    assert capitalize_first('') == ''
    assert capitalize_first('a') == 'A'
    assert capitalize_first('alreadyCapitalized') == 'AlreadyCapitalized'
    assert capitalize_first('123abc') == '123abc'
    assert capitalize_first('python') == 'Python'
    assert capitalize_first('Hello World') == 'Hello World'