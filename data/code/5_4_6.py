def capitalize_first(string):
    if not string:
        return string
    return string[0].upper() + string[1:]

if __name__ == '__main__':
    print(capitalize_first("hello"))
    print(capitalize_first(""))
    print(capitalize_first("a"))
    print(capitalize_first("world"))