def capitalize_first(s):
    if not s:
        return s
    return s[0].upper() + s[1:]

if __name__ == '__main__':
    result = capitalize_first("hello world")
    print(result)