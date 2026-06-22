def capitalize_first(s):
    if not s:
        return s
    first_char = s[0]
    if first_char.isascii() and first_char.islower():
        return first_char.upper() + s[1:]
    return s

if __name__ == '__main__':
    print(capitalize_first("hello"))
    print(capitalize_first("world"))
    print(capitalize_first("a"))
    print(capitalize_first(""))
    print(capitalize_first("HELLO"))
    print(capitalize_first("café"))