def clean_whitespace(text_list):
    return [text.strip() for text in text_list]

if __name__ == '__main__':
    data = ["  hello  ", " world ", "  python  "]
    result = clean_whitespace(data)
    print(result)