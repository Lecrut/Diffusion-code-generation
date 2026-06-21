def word_exists(word_list, target):
    word_set = set(word_list)
    return target in word_set

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry']
    target_word = 'banana'
    print(word_exists(sample_list, target_word))