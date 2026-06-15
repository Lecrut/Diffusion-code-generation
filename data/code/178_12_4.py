def extract_alphabetic_words(sentence):
    words = []
    for char in sentence:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            words.append(char)
    return words
if __name__ == '__main__':
    sample_sentence = "Hello World! This is a test sentence with numbers 123 and symbols @#$"
    result = extract_alphabetic_words(sample_sentence)
    print(result)