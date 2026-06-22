def is_word_long(word):
    length_threshold = 7
    return len(word) > length_threshold
if __name__ == '__main__':
    sample_word_1 = 'programming'
    sample_word_2 = 'cat'
    print(is_word_long(sample_word_1))
    print(is_word_long(sample_word_2))