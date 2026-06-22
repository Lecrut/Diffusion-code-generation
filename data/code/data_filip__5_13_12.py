def capitalize_first_letter(text: str) -> str:
    if not text:
        return text
    return text[0].upper() + text[1:]

if __name__ == '__main__':
    sample_text = "hello world"
    result = capitalize_first_letter(sample_text)
    print(result)
    sample_text_empty = ""
    print(capitalize_first_letter(sample_text_empty))
    sample_text_upper = "WORLD"
    print(capitalize_first_letter(sample_text_upper))