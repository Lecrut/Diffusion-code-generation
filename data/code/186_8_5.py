class WordSorter:
    def sort_by_length(self, words):
        return sorted(words, key=len)

if __name__ == '__main__':
    sorter = WordSorter()
    sample_words = ["apple", "banana", "kiwi", "orange", "grapefruit"]
    sorted_list = sorter.sort_by_length(sample_words)
    print(sorted_list)