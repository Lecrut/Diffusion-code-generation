class WordSorter:
    def sort_words(self, words):
        return sorted(words, reverse=True)

if __name__ == '__main__':
    sorter = WordSorter()
    sample_words = ["apple", "zebra", "banana", "cat", "dog"]
    sorted_list = sorter.sort_words(sample_words)
    print(sorted_list)