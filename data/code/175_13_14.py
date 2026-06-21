def split_sentence(sentence):
    if not isinstance(sentence, str):
        raise ValueError("Input must be a string")
    return sentence.split()

if __name__ == '__main__':
    sample_sentence = "  Hello   world! This is a test sentence. "
    words = split_sentence(sample_sentence)
    print(words)