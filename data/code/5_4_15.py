def capitalize_first_char(s):
    if len(s) == 0:
        return s
    first = s[0]
    if 'a' <= first <= 'z':
        return chr(ord(first) - 32) + s[1:]
    return s

if __name__ == '__main__':
    print(capitalize_first_char("hello"))
    print(capitalize_first_char("WORLD"))
    print(capitalize_first_char(""))
    print(capitalize_first_char("123abc"))
    print(capitalize_first_char("a"))