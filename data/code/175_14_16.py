def tokenize_string(text: str) -> list[str]:
    words = []
    i = 0
    n = len(text)
    
    while i < n:
        if text[i].isspace():
            i += 1
        else:
            start = i
            while i < n and not text[i].isspace():
                i += 1
            words.append(text[start:i])
    
    return words

if __name__ == '__main__':
    sample_string = "  Hello world! This is a test with multiple   spaces. "
    tokens = tokenize_string(sample_string)
    print(tokens)