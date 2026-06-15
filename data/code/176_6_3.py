def find_words_generator(text):
    words = text.split()
    for word in words:
        yield word
if __name__ == '__main__':
    sample_string = "This is a long sample string for testing purposes"
    word_generator = find_words_generator(sample_string)
    found_words = list(word_generator)
    print(found_words)