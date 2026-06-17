def character_type_classifier(char):
    if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
        return 'alphabetic'
    elif '0' <= char <= '9':
        return 'numeric'
    elif ' ' == char:
        return 'whitespace'
    elif char in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~':
        return 'punctuation'
    else:
        return 'symbol'
if __name__ == '__main__':
    test_characters = ['a', '5', '.', ' ', '!', '$', '\n', 'Z', '9', '?', '@']
    for char in test_characters:
        result = character_type_classifier(char)
        print(f"Character: '{char}' -> Type: {result}")