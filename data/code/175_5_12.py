def word_generator(sentence):
    for chunk in sentence.split():
        yield chunk

if __name__ == '__main__':
    sample_sentence = "This is a sample sentence to demonstrate the generator."
    gen = word_generator(sample_sentence)
    for word in gen:
        print(word)