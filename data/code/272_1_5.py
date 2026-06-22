class WordSorter:
    @staticmethod
    def sort_words(word_list):
        return sorted(word_list)

if __name__ == '__main__':
    sample_list = ["banana", "apple", "cherry", "date"]
    sorter = WordSorter()
    sorted_result = sorter.sort_words(sample_list)
    print(sorted_result)