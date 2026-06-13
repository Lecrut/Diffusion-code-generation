def find_words_generator(text):
    words = text.lower().split()
    for word in words:
        if word:
            yield word
if __name__ == '__main__':
    sample_string = "This is a long test string for testing purposes"
    word_generator = find_words_generator(sample_string)
    word_list = list(word_generator)
    print(word_list)