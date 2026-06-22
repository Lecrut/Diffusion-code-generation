def capitalize_first(s):
    if not s:
        return s
    return chr(ord(s[0]) - 32) if 'a' <= s[0] <= 'z' else s

if __name__ == '__main__':
    print(capitalize_first("hello"))
    print(capitalize_first("world"))
    print(capitalize_first(""))
    print(capitalize_first("123abc"))