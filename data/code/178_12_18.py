def tokenize_words(sentence):
    return ' '.join(filter(str.isalpha, sentence.split()))

if __name__ == '__main__':
    sample_sentence = "Hello World! This is a test sentence with numbers 123."
    result = tokenize_words(sample_sentence)
    print(result)