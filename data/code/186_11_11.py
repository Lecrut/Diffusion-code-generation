class WordSorter:
    def __init__(self, words):
        self.words = words

    def sort_desc(self):
        return sorted(self.words, reverse=True)

if __name__ == '__main__':
    sorter = WordSorter(["apple", "zebra", "banana", "cat", "dog"])
    print(sorter.sort_desc())