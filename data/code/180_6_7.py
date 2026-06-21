def validate_word(target, word_list):
    word_set = set(word_list)
    return target in word_set

if __name__ == '__main__':
    sample_target = 'example'
    sample_word_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    print(validate_word(sample_target, sample_word_list))