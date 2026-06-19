def word_lengths(sentence):
    for word in sentence.split():
        yield len(word)

if __name__ == '__main__':
    sample_sentence = "Hello world this is a test"
    for length in word_lengths(sample_sentence):
        print(length)