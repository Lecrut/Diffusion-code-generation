def sort_words(words):
    return sorted(words)

if __name__ == '__main__':
    words_list = ["grape", "orange", "apple", "banana"]
    sorted_list = sort_words(words_list)
    for word in sorted_list:
        print(word)