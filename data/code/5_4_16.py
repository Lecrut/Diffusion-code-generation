def capitalize_first(text):
    if not text:
        return ""
    if len(text) == 0:
        return ""
    if 'a' <= text[0] <= 'z':
        char_code = ord(text[0])
        adjusted_code = char_code - 32
        return chr(adjusted_code) + text[1:]
    if 'A' <= text[0] <= 'Z':
        return text
    return text

if __name__ == '__main__':
    print(capitalize_first("hello"))
    print(capitalize_first("world"))
    print(capitalize_first(""))
    print(capitalize_first("123"))
    print(capitalize_first("a"))