def capitalize_first_letter(text):
    if not text:
        return text
    return text[0].upper() + text[1:]

if __name__ == '__main__':
    assert capitalize_first_letter("") == ""
    assert capitalize_first_letter("hello") == "Hello"
    assert capitalize_first_letter("H") == "H"
    assert capitalize_first_letter("HELLO") == "HELLO"
    assert capitalize_first_letter(" hello") == " hello"
    print(capitalize_first_letter("hello"))
    print(capitalize_first_letter("world"))
    print(capitalize_first_letter("python"))
    print(capitalize_first_letter(""))