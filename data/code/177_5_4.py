def word_generator(text):
    for word in text.split(' '):
        yield word
if __name__ == '__main__':
    long_string = "this is a very long string that needs to be processed efficiently for memory optimization"
    word_gen = word_generator(long_string)
    words = list(word_gen)
    print(words)