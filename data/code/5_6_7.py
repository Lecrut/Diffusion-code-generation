def capitalize_first(s):
    if not s:
        return ""
    if len(s) == 1:
        return s.upper()
    return s[0].upper() + s[1:]

if __name__ == '__main__':
    print(capitalize_first(""))
    print(capitalize_first("a"))
    print(capitalize_first("hello"))
    print(capitalize_first("HELLO"))
    print(capitalize_first("café"))
    print(capitalize_first("österreich"))