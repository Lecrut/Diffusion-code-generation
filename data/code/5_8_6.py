def capitalize_first_letter(text: str) -> str:
    if not text:
        return text
    if len(text) == 1:
        return text.upper()
    return text[0].upper() + text[1:]

if __name__ == '__main__':
    assert capitalize_first_letter("") == ""
    assert capitalize_first_letter("a") == "A"
    assert capitalize_first_letter("hello") == "Hello"
    assert capitalize_first_letter("123abc") == "123abc"
    assert capitalize_first_letter(" already capitalized") == " already capitalized"
    assert capitalize_first_letter("lowercase input") == "Lowercase input"
    print(capitalize_first_letter(""))
    print(capitalize_first_letter("a"))
    print(capitalize_first_letter("hello"))
    print(capitalize_first_letter("123abc"))
    print(capitalize_first_letter(" already capitalized"))
    print(capitalize_first_letter("lowercase input"))