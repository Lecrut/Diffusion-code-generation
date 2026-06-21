class WordSorter:
    @staticmethod
    def sort_by_length(words):
        return sorted(words, key=len)

if __name__ == '__main__':
    sample_words = ["apple", "banana", "kiwi", "orange", "grapefruit"]
    sorter = WordSorter()
    sorted_list = sorter.sort_by_length(sample_words)
    print(sorted_list)