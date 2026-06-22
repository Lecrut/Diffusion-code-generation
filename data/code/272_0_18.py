class WordSorter:
    @staticmethod
    def sort_words(word_list):
        return sorted(word_list)

if __name__ == '__main__':
    sample_words = ["banana", "apple", "cherry", "date", "elderberry"]
    sorter = WordSorter()
    sorted_result = sorter.sort_words(sample_words)
    print(*sorted_result)