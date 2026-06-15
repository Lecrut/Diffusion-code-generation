class WordSorter:
    def sort_list(self, word_list):
        return sorted(word_list)
if __name__ == '__main__':
    sorter = WordSorter()
    sample_words = ["apple", "zebra", "banana", "cat", "dog"]
    sorted_words = sorter.sort_list(sample_words)
    print(sorted_words)