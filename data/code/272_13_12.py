def sort_words(word_list):
    return sorted(word_list)

if __name__ == '__main__':
    words = ["grape", "orange", "apple", "banana", "mango"]
    sorted_words = sort_words(words)
    print("Original list of words:", words)
    print("Sorted list of words:", sorted_words)