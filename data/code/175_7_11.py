def strip_and_split(sentence):
    return [token.strip() for token in sentence.split() if token.strip()]

if __name__ == '__main__':
    sample_sentence = "  Hello   world! This is a test.  "
    print(strip_and_split(sample_sentence))