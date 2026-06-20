def capitalize_first(s):
    if len(s) == 0:
        return s
    return s[0].upper() + s[1:]

if __name__ == '__main__':
    print(capitalize_first("hello"))
    print(capitalize_first(""))
    print(capitalize_first("WORLD"))
    print(capitalize_first("123abc"))