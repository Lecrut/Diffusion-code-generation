def validate_word(target, word_list):
    word_set = set(word_list)
    return target in word_set

if __name__ == '__main__':
    sample_target = 'apple'
    sample_word_list = ['banana', 'apple', 'cherry']
    print(validate_word(sample_target, sample_word_list))