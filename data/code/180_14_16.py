def word_exists(word_list, search_word):
    return search_word in set(word_list)
if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry']
    print(word_exists(sample_list, 'banana'))
    print(word_exists(sample_list, 'grape'))