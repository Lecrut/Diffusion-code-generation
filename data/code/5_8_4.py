def capitalize_first_letter(text):
    if not text:
        return text
    return text[0].upper() + text[1:]

if __name__ == '__main__':
    assert capitalize_first_letter("hello") == "Hello"
    assert capitalize_first_letter("WORLD") == "WORLD"
    assert capitalize_first_letter("") == ""
    assert capitalize_first_letter("a") == "A"
    assert capitalize_first_letter(" test") == " Test"
    result = capitalize_first_letter("python is fun")
    print(result)