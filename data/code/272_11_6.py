class WordSorter:
    @staticmethod
    def sort(word_list):
        return sorted(word_list)

if __name__ == '__main__':
    sample_words = ["banana", "apple", "cherry", "date", "elderberry"]
    sorter = WordSorter()
    sorted_result = sorter.sort(sample_words)
    print(sorted_result)