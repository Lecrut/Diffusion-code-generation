def capitalize_first(s):
    if len(s) == 0:
        return s
    first = s[0]
    if first >= 'a' and first <= 'z':
        first = chr(ord(first) - 32)
    return first + s[1:]

if __name__ == '__main__':
    print(capitalize_first("hello"))
    print(capitalize_first(""))
    print(capitalize_first("WORLD"))
    print(capitalize_first("123test"))
    print(capitalize_first("a"))