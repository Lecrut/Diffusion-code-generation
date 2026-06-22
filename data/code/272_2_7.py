def sort_words(word_list):
    return sorted(word_list)

if __name__ == '__main__':
    words_to_sort = ["banana", "apple", "cherry", "date"]
    sorted_words = sort_words(words_to_sort)
    print(sorted_words)