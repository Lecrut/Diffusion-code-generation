def capitalize_first(s: str) -> str:
    return s[0].upper() + s[1:].lower() if s else ""

if __name__ == '__main__':
    print(capitalize_first("hello"))
    print(capitalize_first("WORLD"))
    print(capitalize_first("hElLo"))
    print(capitalize_first(""))
    print(capitalize_first("a"))