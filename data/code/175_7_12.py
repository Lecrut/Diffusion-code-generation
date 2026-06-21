def separate_words(sentence):
    return [word.strip() for word in sentence.split() if word.strip()]

if __name__ == '__main__':
    sample_sentence = "  Hello   world! This is a test.  "
    print(separate_words(sample_sentence))