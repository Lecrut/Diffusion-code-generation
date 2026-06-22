def capitalize_first(s: str) -> str:
    if not s:
        return ""
    first = s[0]
    rest = s[1:]
    if first.isupper():
        return s
    if first.isascii():
        return first.upper() + rest
    return first.upper() + rest

if __name__ == '__main__':
    print(capitalize_first("hello"))
    print(capitalize_first("world"))
    print(capitalize_first("A"))
    print(capitalize_first("a"))
    print(capitalize_first(""))
    print(capitalize_first("café"))
    print(capitalize_first("123abc"))
    print(capitalize_first("ñandú"))