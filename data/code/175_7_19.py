def separate_words(sentence):
    return [token.strip() for token in sentence.split() if token.strip()]

if __name__ == '__main__':
    sample_sentence1 = "  I don't know where we are  "
    sample_sentence2 = "She won't go if you don't like it"
    print(separate_words(sample_sentence1))
    print(separate_words(sample_sentence2))