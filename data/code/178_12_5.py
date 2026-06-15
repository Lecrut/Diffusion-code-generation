def extract_alphabetic_words(sentence):
    words = []
    for char in sentence:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            words.append(char)
    return list(set(words))
if __name__ == '__main__':
    sample_sentence1 = "Hello World! This is a test sentence."
    result1 = extract_alphabetic_words(sample_sentence1)
    print(result1)
    sample_sentence2 = "123 abc-def GHI jklm"
    result2 = extract_alphabetic_words(sample_sentence2)
    print(result2)
    sample_sentence3 = "Programming is fun and challenging"
    result3 = extract_alphabetic_words(sample_sentence3)
    print(result3)