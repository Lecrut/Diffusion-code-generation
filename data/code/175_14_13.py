def tokenize_string(text: str) -> list[str]:
    if not isinstance(text, str):
        raise ValueError('Input must be a string')
    text = text.strip()
    words = text.split(' ')
    filtered_words = [word for word in words if word]
    return filtered_words
if __name__ == '__main__':
    sample_string = '  Hello world! This is a test with multiple   spaces. '
    tokens = tokenize_string(sample_string)
    print(tokens)