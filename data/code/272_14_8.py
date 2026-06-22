class WordSorter:
    def sort(self, words):
        return sorted(words)

if __name__ == '__main__':
    sorter = WordSorter()
    sample_words = ["banana", "apple", "cherry"]
    print(sorter.sort(sample_words))