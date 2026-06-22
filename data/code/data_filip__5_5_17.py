def capitalize_first_letter(text: str) -> str:
    if not text:
        return text
    return "".join([text[0].upper(), text[1:]])

if __name__ == '__main__':
    sample_data = "hello world"
    result = capitalize_first_letter(sample_data)
    print(result)