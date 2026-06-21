def split_sentence(sentence):
    if not isinstance(sentence, str) or not sentence.strip():
        raise ValueError("Input must be a non-empty string.")
    return sentence.split()

if __name__ == '__main__':
    sample_sentence = "  Hello   world! This is a test sentence. "
    try:
        words = split_sentence(sample_sentence)
        print(words)
    except ValueError as e:
        print(e)