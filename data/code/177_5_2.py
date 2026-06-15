def word_generator(text):
    for word in text.split(' '):
        yield word
if __name__ == '__main__':
    long_string = "this is a very long string designed to test the generator's memory efficiency when dealing with extremely large amounts of text and ensuring that we only process the data as it is yielded without loading the entire list of words into memory at once"
    word_gen = word_generator(long_string)
    words = list(word_gen)
    print(words)