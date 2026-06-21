def word_exists(word_list, search_word):
    word_set = set(word_list)
    return search_word in word_set

if __name__ == '__main__':
    sample_words = ['apple', 'banana', 'cherry']
    search_term = 'banana'
    print(word_exists(sample_words, search_term))