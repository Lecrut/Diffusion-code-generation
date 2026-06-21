def tokenize_string(text: str) -> list[str]:
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    return [word for word in text.split() if word]

if __name__ == '__main__':
    sample_string = "  Hello world! This is a test with multiple   spaces. "
    tokens = tokenize_string(sample_string)
    print(tokens)