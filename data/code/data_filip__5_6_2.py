def capitalize_first(text):
    if not text:
        return ""
    
    first_char = text[0]
    rest = text[1:]
    
    if first_char.isupper() or not first_char.isalpha():
        return text
    
    if first_char.isascii():
        return first_char.upper() + rest
    
    try:
        return first_char.upper() + rest
    except AttributeError:
        return text

if __name__ == '__main__':
    print(capitalize_first("hello"))
    print(capitalize_first("world"))
    print(capitalize_first(""))
    print(capitalize_first("1abc"))
    print(capitalize_first("a"))
    print(capitalize_first("HELLO"))
    print(capitalize_first("café"))