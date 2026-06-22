def word_lengths(sentence):
    for word in sentence.split():
        yield len(word)

if __name__ == '__main__':
    sample_sentence = "This is a test sentence"
    lengths_generator = word_lengths(sample_sentence)
    for length in lengths_generator:
        print(length)