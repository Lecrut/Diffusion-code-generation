def capitalize_first(string: str) -> str:
    if not string:
        return string
    return string[0].upper() + string[1:]

if __name__ == '__main__':
    print(capitalize_first("hello"))
    print(capitalize_first("world"))
    print(capitalize_first(""))
    print(capitalize_first("a"))
    assert capitalize_first("hello") == "Hello"
    assert capitalize_first("world") == "World"
    assert capitalize_first("") == ""
    assert capitalize_first("a") == "A"
    assert capitalize_first("123") == "123"
    assert capitalize_first("abc") == "Abc"