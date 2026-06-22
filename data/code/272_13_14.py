class WordSorter:
    @staticmethod
    def sort_words(words):
        return sorted(words)

if __name__ == '__main__':
    sample_words = ["banana", "apple", "cherry"]
    sorter = WordSorter()
    sorted_words = sorter.sort_words(sample_words)
    print("Alphabetically sorted list:", sorted_words)