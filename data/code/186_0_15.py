class WordSorter:
    def __init__(self, word_list):
        self.word_list = word_list

    def sort(self):
        return sorted(self.word_list)

if __name__ == '__main__':
    sorter = WordSorter(["banana", "apple", "cherry", "date", "elderberry"])
    sorted_words = sorter.sort()
    print(sorted_words)