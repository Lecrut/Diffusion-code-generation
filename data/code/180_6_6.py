def validate_word(target, string_list):
    word_set = set(string_list)
    return target in word_set

if __name__ == '__main__':
    sample_target = 'example'
    sample_string_list = ['apple', 'banana', 'cherry', 'date', 'example']
    print(validate_word(sample_target, sample_string_list))