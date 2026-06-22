class WordSorter:
    def __init__(self, words):
        self.words = words

    def sort(self):
        return sorted(self.words)

if __name__ == '__main__':
    sorter = WordSorter(["banana", "apple", "cherry", "date"])
    print(sorter.sort())