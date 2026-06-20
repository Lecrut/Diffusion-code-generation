def capitalize_first(s):
    if not s:
        return s
    first = ord(s[0])
    if 97 <= first <= 122:
        first -= 32
    return chr(first) + s[1:]

if __name__ == '__main__':
    print(capitalize_first(''))
    print(capitalize_first('hello'))
    print(capitalize_first('WORLD'))
    print(capitalize_first('123abc'))
    print(capitalize_first('z'))