class WordSorter:
    def sort(self, word_list):
        return sorted(word_list)

if __name__ == '__main__':
    sorter = WordSorter()
    words = ["banana", "apple", "zebra", "cat", "dog"]
    sorted_words = sorter.sort(words)
    print(sorted_words)

    another_sorter = WordSorter()
    more_words = ["cherry", "date", "elderberry"]
    even_more_sorted_words = another_sorter.sort(more_words)
    print(even_more_sorted_words)