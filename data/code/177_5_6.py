def word_generator(text):
    for word in text.split(' '):
        yield word
if __name__ == '__main__':
    long_string = "this is a very long string designed to test the generator's memory efficiency when processing extremely large amounts of text data and ensuring that we only yield words one by one without storing the entire list of words in memory at once"
    word_gen = word_generator(long_string)
    words_list = []
    for word in word_gen:
        words_list.append(word)
    print(words_list)