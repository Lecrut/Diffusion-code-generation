def word_generator(sentence):
    for word in sentence.split():
        yield word
if __name__ == '__main__':
    sample_sentence = 'This is a sample sentence to demonstrate the memory-efficient generator.'
    gen = word_generator(sample_sentence)
    for _ in range(5):
        print(next(gen))