def word_lengths(sentence):
    for word in sentence.split():
        yield len(word)

if __name__ == '__main__':
    sample_sentence = "This is a test sentence with various lengths"
    for length in word_lengths(sample_sentence):
        print(length)