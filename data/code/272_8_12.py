class WordSorter:
    def __init__(self, words):
        self.words = words

    def sort_words(self):
        return sorted(self.words)

if __name__ == '__main__':
    sorter = WordSorter(["banana", "apple", "cherry", "date", "elderberry"])
    sorted_list = sorter.sort_words()
    print("Sorted list of words:")
    for word in sorted_list:
        print(word)