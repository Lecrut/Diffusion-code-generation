def capitalize_first(text):
    if not text:
        return text
    return text[0].upper() + text[1:]

if __name__ == '__main__':
    print(capitalize_first("hello world"))
    print(capitalize_first("python"))
    print(capitalize_first(""))