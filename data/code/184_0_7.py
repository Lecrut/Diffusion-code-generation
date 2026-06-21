def word_exists(word_list, search_word):
    word_set = set(word_list)
    return search_word in word_set

if __name__ == '__main__':
    sample_data = ["apple", "banana", "cherry", "date"]
    search_term = "banana"
    print(word_exists(sample_data, search_term))