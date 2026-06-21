def is_word_present(words_set, word):
    return word.lower() in words_set

if __name__ == '__main__':
    sample_words = {'apple', 'banana', 'cherry'}
    word_to_check1 = "Apple"
    print(f"'{word_to_check1}' in set: {is_word_present(sample_words, word_to_check1)}")
    word_to_check2 = "orange"
    print(f"'{word_to_check2}' in set: {is_word_present(sample_words, word_to_check2)}")