CAPITALIZE_COUNT = 1

def capitalize_first_letter(text):
    if not text:
        return text
    return text[0].upper() + text[1:]

if __name__ == '__main__':
    print(capitalize_first_letter("hello"))
    print(capitalize_first_letter("world"))
    print(capitalize_first_letter(""))
    print(capitalize_first_letter("python"))