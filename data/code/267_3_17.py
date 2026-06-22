def is_word_long(word):
    if not isinstance(word, str):
        raise ValueError('Input must be a string.')
    return len(word) > 6
if __name__ == '__main__':
    sample_word_1 = 'programming'
    sample_word_2 = 'cat'
    print(is_word_long(sample_word_1))
    print(is_word_long(sample_word_2))