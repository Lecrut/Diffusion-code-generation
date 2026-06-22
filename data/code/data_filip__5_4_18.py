def capitalize_first_letter(s):
    if not s:
        return s
    first_char = s[0]
    if ord('a') <= ord(first_char) <= ord('z'):
        new_first = chr(ord(first_char) - 32)
        return new_first + s[1:]
    return s

if __name__ == '__main__':
    print(capitalize_first_letter(''))
    print(capitalize_first_letter('hello'))
    print(capitalize_first_letter('world'))
    print(capitalize_first_letter('H ello'))
    print(capitalize_first_letter('a'))
    print(capitalize_first_letter('A'))
    print(capitalize_first_letter('123'))
    print(capitalize_first_letter(' python '))