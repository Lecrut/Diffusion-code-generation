def capitalize_first_letter(s: str) -> str:
    if not s:
        return s
    return s[0].upper() + s[1:]

if __name__ == '__main__':
    print(capitalize_first_letter("hello"))
    print(capitalize_first_letter("world"))
    print(capitalize_first_letter(""))
    print(capitalize_first_letter("a"))