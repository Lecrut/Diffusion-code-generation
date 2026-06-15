def sort_words_by_length(words):
    return sorted(words, key=len, reverse=True)
if __name__ == '__main__':
    word_list = ["apple", "banana", "kiwi", "orange", "grapefruit"]
    sorted_list = sort_words_by_length(word_list)
    print(sorted_list)