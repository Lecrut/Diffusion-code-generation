def is_word_long(word):
    length_threshold = 6
    return len(word) > length_threshold

if __name__ == '__main__':
    sample_word_1 = 'example'
    sample_word_2 = 'hi'
    print(is_word_long(sample_word_1))
    print(is_word_long(sample_word_2))