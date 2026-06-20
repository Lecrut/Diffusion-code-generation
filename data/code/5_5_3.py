def capitalize_first_char(text: str) -> str:
    if not text:
        return text
    return "".join([text[0].upper(), *text[1:]])

if __name__ == '__main__':
    sample_data = ["hello world", "python", "a", "", "123abc", "ALREADY_UPPER"]
    for s in sample_data:
        print(capitalize_first_char(s))