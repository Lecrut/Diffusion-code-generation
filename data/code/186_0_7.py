def sort_words(word_list):
    return sorted(word_list)

if __name__ == '__main__':
    unsorted_words = ["grape", "orange", "apple", "banana", "cherry"]
    sorted_words = sort_words(unsorted_words)
    print(sorted_words)