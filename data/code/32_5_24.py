def word_lengths_generator(sentence):
    words = sentence.split()
    for word in words:
        yield len(word)

if __name__ == '__main__':
    sample_sentence = "This is a test sentence"
    lengths_gen = word_lengths_generator(sample_sentence)
    for length in lengths_gen:
        print(length)