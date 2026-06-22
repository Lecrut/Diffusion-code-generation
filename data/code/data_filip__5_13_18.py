def capitalize_first_letter(s):
    if not s:
        return ""
    return s[0].upper() + s[1:]

if __name__ == '__main__':
    print(capitalize_first_letter("hello world"))
    print(capitalize_first_letter("123abc"))
    print(capitalize_first_letter(""))