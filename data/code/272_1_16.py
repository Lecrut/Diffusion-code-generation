class WordSorter:
    @staticmethod
    def sort(words):
        return sorted(words)

if __name__ == '__main__':
    sample_words = ["banana", "apple", "cherry"]
    sorter = WordSorter()
    sorted_list = sorter.sort(sample_words)
    print(sorted_list)