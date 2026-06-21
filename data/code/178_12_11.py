def tokenize_sentence(sentence):
    cleaned = ''.join(char for char in sentence if char.isalpha() or char.isspace())
    words = cleaned.split()
    return list(dict.fromkeys(words))

if __name__ == '__main__':
    sample_sentence = "Hello, World! This is a test sentence with numbers 123."
    result = tokenize_sentence(sample_sentence)
    print(result)