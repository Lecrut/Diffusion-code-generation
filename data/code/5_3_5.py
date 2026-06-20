def capitalize_first_if_alphanumeric(s):
    if not s:
        return s
    first_char = s[0]
    if first_char.isalnum():
        return first_char.upper() + s[1:]
    return s

if __name__ == '__main__':
    print(capitalize_first_if_alphanumeric("hello"))
    print(capitalize_first_if_alphanumeric("123abc"))
    print(capitalize_first_if_alphanumeric("!hello"))
    print(capitalize_first_if_alphanumeric(""))
    print(capitalize_first_if_alphanumeric("a"))
    print(capitalize_first_if_alphanumeric("ALREADY_CAPITAL"))