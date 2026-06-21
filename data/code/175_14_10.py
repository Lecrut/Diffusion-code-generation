def tokenize_string(text: str) -> list[str]:
    words = []
    in_word = False
    for char in text:
        if char.isalpha():
            if not in_word:
                in_word = True
                words.append(char)
            else:
                words[-1] += char
        elif in_word:
            in_word = False
    return words

if __name__ == '__main__':
    sample_string = "  Hello world! This is a test with multiple   spaces. "
    tokens = tokenize_string(sample_string)
    print(tokens)