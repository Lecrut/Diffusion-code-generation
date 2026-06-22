class WordSorter:
    def sort_words(self, word_list):
        return sorted(word_list)

if __name__ == '__main__':
    sorter = WordSorter()
    sample_words = ["banana", "apple", "cherry", "date", "elderberry"]
    sorted_result = sorter.sort_words(sample_words)
    print(sorted_result)