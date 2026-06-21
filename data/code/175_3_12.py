if __name__ == '__main__':
    sample_sentence = "  Hello   world! This is a test, with various spaces and punctuation.  "
    words = [word for word in sample_sentence.split() if word]
    print(words)