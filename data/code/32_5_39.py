def word_lengths(sentence):
    words = sentence.split()
    for word in words:
        yield len(word)

if __name__ == '__main__':
    sample_sentence = "Hello world this is a test"
    lengths_generator = word_lengths(sample_sentence)
    for length in lengths_generator:
        print(length)