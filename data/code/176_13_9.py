def get_words(sentence):
    words = sentence.lower().split()
    return words

if __name__ == '__main__':
    sample_sentence = "Hello World! This is a test."
    print(get_words(sample_sentence))