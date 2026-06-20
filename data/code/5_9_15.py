def capitalize_first(s):
    if not s:
        return s
    return s[0].upper() + s[1:].lower()

if __name__ == '__main__':
    print(capitalize_first("hELLo WoRLd"))
    print(capitalize_first(""))
    print(capitalize_first("a"))
    print(capitalize_first("PYTHON"))