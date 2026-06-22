def capitalize_first_letter(text):
    if not text:
        return text
    return text[0].upper() + text[1:]

if __name__ == '__main__':
    sample_string = "hello world"
    result = capitalize_first_letter(sample_string)
    print(result)
    print(capitalize_first_letter("python is awesome"))
    print(capitalize_first_letter(""))