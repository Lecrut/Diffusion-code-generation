def capitalize_first(s):
    if not s:
        return s
    first = s[0]
    if 'a' <= first <= 'z':
        return chr(ord(first) - 32) + s[1:]
    return s

if __name__ == '__main__':
    print(capitalize_first(''))
    print(capitalize_first('hello'))
    print(capitalize_first('Hello'))
    print(capitalize_first('a'))
    print(capitalize_first('Z'))
    print(capitalize_first('123abc'))