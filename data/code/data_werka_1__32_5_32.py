def word_lengths(sentence):
    for word in sentence.split():
        yield len(word)

if __name__ == '__main__':
    sample_sentence = "The quick brown fox jumps over the lazy dog"
    lengths = list(word_lengths(sample_sentence))
    print(lengths)