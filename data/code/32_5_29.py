def word_length_generator(sentence):
    for word in sentence.split():
        yield len(word)

if __name__ == '__main__':
    sample_sentence = "Hello world this is a test"
    generator = word_length_generator(sample_sentence)
    for length in generator:
        print(length)