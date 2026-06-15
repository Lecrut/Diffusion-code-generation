def find_words_generator(text):
    words = text.split()
    for word in words:
        yield word
if __name__ == '__main__':
    long_string = "this is a test string for testing purposes and it contains many words"
    word_generator = find_words_generator(long_string)
    found_words = list(word_generator)
    print(found_words)