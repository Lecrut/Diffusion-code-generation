class WordSorter:
    def __init__(self, words):
        self.words = words

    def filter_and_sort(self):
        filtered_words = [item for item in self.words if isinstance(item, str)]
        return sorted(filtered_words)

if __name__ == '__main__':
    sorter = WordSorter(["banana", "apple", "cherry", "date", "elderberry"])
    sorted_words = sorter.filter_and_sort()
    print("Sorted list of words:", sorted_words)