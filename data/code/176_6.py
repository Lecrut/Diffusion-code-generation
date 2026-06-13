def find_words_generator(text):
    for word in text.split():
        yield word
if __name__ == '__main__':
    sample_string = "This is a long sentence for testing purposes and memory efficiency"
    word_generator = find_words_generator(sample_string)
    word_list = list(word_generator)
    print(word_list)