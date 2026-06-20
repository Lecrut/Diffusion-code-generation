def capitalize_first_letter(s):
    return s[:1].upper() + s[1:] if s else s

if __name__ == '__main__':
    print(capitalize_first_letter("hello"))
    print(capitalize_first_letter("world"))
    print(capitalize_first_letter(""))
    print(capitalize_first_letter("a"))
    print(capitalize_first_letter("ALREADY"))