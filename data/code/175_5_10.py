def word_generator(sentence):
    for word in sentence.split():
        yield word

if __name__ == '__main__':
    sample_sentence = "This is a sample sentence to demonstrate the generator."
    gen = word_generator(sample_sentence)
    for word in gen:
        print(word)