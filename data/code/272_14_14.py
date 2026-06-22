class WordSorter:
    @staticmethod
    def sort(words):
        return sorted(words)

if __name__ == '__main__':
    sample_words = ["banana", "apple", "cherry", "date"]
    sorter = WordSorter()
    print(sorter.sort(sample_words))