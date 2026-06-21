def tokenize_string(text: str) -> list[str]:
    words = []
    in_word = False
    for char in text:
        if char.isalpha():
            if not in_word:
                words.append('')
                in_word = True
            words[-1] += char
        elif in_word:
            in_word = False
    if in_word:
        words.append('')
    return [word.strip() for word in words if word]

if __name__ == '__main__':
    sample_string = "  Hello world! This is a test with multiple   spaces. "
    tokens = tokenize_string(sample_string)
    print(tokens)