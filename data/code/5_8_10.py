def capitalize_first(s: str) -> str:
    if not s:
        return s
    return s[0].upper() + s[1:]

if __name__ == '__main__':
    result1 = capitalize_first('hello')
    print(result1)
    assert result1 == 'Hello', f"Expected 'Hello', got '{result1}'"

    result2 = capitalize_first('world')
    print(result2)
    assert result2 == 'World', f"Expected 'World', got '{result2}'"

    result3 = capitalize_first('')
    print(repr(result3))
    assert result3 == '', f"Expected '', got '{result3}'"

    result4 = capitalize_first('a')
    print(result4)
    assert result4 == 'A', f"Expected 'A', got '{result4}'"

    result5 = capitalize_first('already Capitalized')
    print(result5)
    assert result5 == 'Already Capitalized', f"Expected 'Already Capitalized', got '{result5}'"

    result6 = capitalize_first('123abc')
    print(result6)
    assert result6 == '123abc', f"Expected '123abc', got '{result6}'"

    print('All assertions passed.')