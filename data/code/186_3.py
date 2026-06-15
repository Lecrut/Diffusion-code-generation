class WordSorter:
    def __init__(self, words):
        self.words = words
    def sort_reverse_alphabetical(self):
        self.words.sort(reverse=True)
        return self.words
if __name__ == '__main__':
    sample_words = ["apple", "zebra", "banana", "cat", "dog"]
    sorter = WordSorter(sample_words)
    sorted_words = sorter.sort_reverse_alphabetical()
    print(sorted_words)