def capitalize_first(text):
    if not text:
        return ""
    if len(text) == 1:
        return text.upper()
    first = text[0].upper()
    rest = text[1:]
    if first != text[0]:
        return first + rest
    if rest == "":
        return text
    return text[0] + rest.upper() if first == text[0].lower() else first + rest[1:] if len(rest) > 1 else first + rest

if __name__ == '__main__':
    print(capitalize_first("hello"))
    print(capitalize_first("world"))
    print(capitalize_first("a"))
    print(capitalize_first(""))
    print(capitalize_first("ñ"))
    print(capitalize_first("ü"))