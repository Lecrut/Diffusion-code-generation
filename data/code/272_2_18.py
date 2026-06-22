class WordSorter:
    @staticmethod
    def sort(word_list):
        return sorted(word_list)

if __name__ == '__main__':
    sample_words = ["banana", "apple", "cherry"]
    sorter = WordSorter()
    sorted_words = sorter.sort(sample_words)
    print(sorted_words)