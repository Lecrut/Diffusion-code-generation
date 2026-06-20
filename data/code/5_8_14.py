def capitalize_first(s: str) -> str:
    if not s:
        return s
    return s[0].upper() + s[1:]

if __name__ == '__main__':
    print(capitalize_first("hello"))
    print(capitalize_first("world"))
    print(capitalize_first(""))
    print(capitalize_first("a"))
    assert capitalize_first("hello") == "Hello"
    assert capitalize_first("") == ""
    assert capitalize_first("a") == "A"