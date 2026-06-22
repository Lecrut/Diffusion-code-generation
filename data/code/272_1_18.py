class WordSorter:
    def sort(self, word_list):
        return sorted(word_list)

if __name__ == '__main__':
    sorter = WordSorter()
    sample_list = ["banana", "apple", "cherry", "date"]
    sorted_result = sorter.sort(sample_list)
    print(sorted_result)