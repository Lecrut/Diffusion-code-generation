class WordSorter:
    def __init__(self, word_list):
        self.word_list = word_list

    def sort_words(self):
        return sorted(self.word_list, reverse=True)

if __name__ == '__main__':
    sorter = WordSorter(["banana", "apple", "date", "cherry", "elderberry"])
    sorted_words = sorter.sort_words()
    print(sorted_words)