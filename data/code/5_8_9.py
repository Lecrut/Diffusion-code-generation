def capitalize_first_letter(s):
    if not s:
        return s
    return s[0].upper() + s[1:]

if __name__ == '__main__':
    assert capitalize_first_letter("hello") == "Hello"
    assert capitalize_first_letter("world") == "World"
    assert capitalize_first_letter("") == ""
    assert capitalize_first_letter("a") == "A"
    assert capitalize_first_letter("already Capitalized") == "Already Capitalized"
    assert capitalize_first_letter("123abc") == "123abc"
    assert capitalize_first_letter("test with spaces") == "Test with spaces"
    print(capitalize_first_letter("hello"))
    print(capitalize_first_letter("world"))
    print(capitalize_first_letter(""))
    print(capitalize_first_letter("a"))
    print(capitalize_first_letter("already Capitalized"))
    print(capitalize_first_letter("123abc"))
    print(capitalize_first_letter("test with spaces"))