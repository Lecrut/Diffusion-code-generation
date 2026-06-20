def capitalize_first(s):
    if s == '':
        return s
    first_char = s[0]
    if 'a' <= first_char <= 'z':
        return chr(ord(first_char) - 32) + s[1:]
    return s

if __name__ == '__main__':
    print(capitalize_first('hello'))
    print(capitalize_first(''))
    print(capitalize_first('world'))
    print(capitalize_first('123test'))
    print(capitalize_first('Already Capitalized'))