class WordSorter:
    def __init__(self, words):
        self.words = [word for word in words if isinstance(word, str)]

    def sort_words(self):
        return sorted(self.words)

if __name__ == '__main__':
    sorter = WordSorter(["banana", "apple", "cherry", "date", "elderberry"])
    print("Original list of words:", ["banana", "apple", "cherry", "date", "elderberry"])
    print("Sorted list of words:", sorter.sort_words())