def validate_word(word_list, target):
    word_set = set(word_list)
    return target in word_set

if __name__ == '__main__':
    sample_words = ['apple', 'banana', 'cherry']
    target_word = 'banana'
    print(validate_word(sample_words, target_word))