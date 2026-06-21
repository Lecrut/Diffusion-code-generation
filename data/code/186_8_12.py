class WordSorter:
    def __init__(self):
        self.sample_words = ["apple", "banana", "kiwi", "orange", "grapefruit"]

    @staticmethod
    def sort_by_length(words):
        return sorted(words, key=len)

if __name__ == '__main__':
    sorter = WordSorter()
    sorted_list = sorter.sort_by_length(sorter.sample_words)
    print(sorted_list)