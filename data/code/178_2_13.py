def tokenize_sentence(sentence, delimiter):
    return sentence.split(delimiter)

if __name__ == '__main__':
    sample_sentence = "This is a sample, sentence for testing word extraction."
    delimiter = ","
    words = tokenize_sentence(sample_sentence, delimiter)
    print(words)