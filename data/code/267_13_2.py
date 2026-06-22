def filter_long_words(sentence):
    long_words = [word for word in sentence.split() if len(word) > 3]
    return long_words

if __name__ == '__main__':
    sample_sentence = "The quick brown fox jumps over the lazy dog"
    result = filter_long_words(sample_sentence)
    print(result)