def capitalize_first(s: str) -> str:
    if not s:
        return s
    return s[0].upper() + s[1:]

if __name__ == '__main__':
    assert capitalize_first("hello") == "Hello"
    assert capitalize_first("") == ""
    assert capitalize_first("a") == "A"
    assert capitalize_first("123abc") == "123abc"
    assert capitalize_first("wORLD") == "WORLD"
    
    print(capitalize_first("hello world"))
    print(capitalize_first(""))
    print(capitalize_first("python"))