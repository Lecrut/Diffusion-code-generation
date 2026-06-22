def filter_long_words(sentence):
    return [word for word in sentence.split() if len(word) > 3]

if __name__ == '__main__':
    sample_sentence = "Hello world this is a test"
    long_words = filter_long_words(sample_sentence)
    print(long_words)