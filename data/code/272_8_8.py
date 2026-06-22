class WordSorter:
    @staticmethod
    def sort_words(word_list):
        return sorted(word_list)

if __name__ == '__main__':
    word_sequence = ["banana", "apple", "cherry", "date", "elderberry"]
    sorter = WordSorter()
    sorted_words = sorter.sort_words(word_sequence)
    print("Sorted list of words:")
    for word in sorted_words:
        print(word)