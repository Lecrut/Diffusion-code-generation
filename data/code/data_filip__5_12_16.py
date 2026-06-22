def capitalize_first(s):
    return s[:1].upper() + s[1:].lower()

if __name__ == '__main__':
    print(capitalize_first("hello"))
    print(capitalize_first("WORLD"))
    print(capitalize_first("hElLo WoRLd"))
    print(capitalize_first(""))
    print(capitalize_first("a"))