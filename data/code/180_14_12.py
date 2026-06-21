def word_exists(word_list, target_word):
    return target_word in set(word_list)

if __name__ == '__main__':
    sample_words = ['apple', 'banana', 'cherry']
    search_word = 'banana'
    print(word_exists(sample_words, search_word))