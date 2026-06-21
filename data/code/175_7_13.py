def strip_and_filter(tokens):
    return [token.strip() for token in tokens if token.strip()]

if __name__ == '__main__':
    sample_sentence1 = "  This is a test sentence.  "
    sample_sentence2 = "Another example, with more   spaces."

    words1 = strip_and_filter(sample_sentence1.split())
    words2 = strip_and_filter(sample_sentence2.split())

    print(words1)
    print(words2)