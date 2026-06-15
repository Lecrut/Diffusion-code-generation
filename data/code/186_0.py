def sort_words(word_list):
    return sorted(word_list)
if __name__ == '__main__':
    unsorted_words = ["banana", "apple", "cherry", "date", "elderberry"]
    sorted_words = sort_words(unsorted_words)
    print(sorted_words)