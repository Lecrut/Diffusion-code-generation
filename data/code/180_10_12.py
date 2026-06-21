def is_word_present(words, word):
    return word in words

if __name__ == '__main__':
    sample_words = {'apple', 'banana', 'cherry'}
    word_to_check = 'banana'
    print(f"'{word_to_check}' in set: {is_word_present(sample_words, word_to_check)}")