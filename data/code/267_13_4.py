def filter_long_words(sentence):
    return [word for word in sentence.split() if len(word) > 3]

if __name__ == '__main__':
    sample_sentence = "This is a test sentence with some long words"
    print(filter_long_words(sample_sentence))