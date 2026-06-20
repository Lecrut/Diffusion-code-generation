def capitalize_first(s):
    if not s:
        return ""
    first_char = s[0]
    if first_char.isascii():
        if first_char.islower():
            return first_char.upper() + s[1:]
        return s
    else:
        upper_first = first_char.upper()
        if len(s) > 1:
            return upper_first + s[1:]
        return upper_first

if __name__ == '__main__':
    print(capitalize_first("hello"))
    print(capitalize_first("a"))
    print(capitalize_first(""))
    print(capitalize_first("already Capital"))
    print(capitalize_first("ñandú"))
    print(capitalize_first("123abc"))