class WordSorter:
    def sort(self, word_list):
        return sorted(word_list)
if __name__ == '__main__':
    sorter = WordSorter()
    sample_list = ["banana", "apple", "cherry", "date", "elderberry"]
    sorted_list = sorter.sort(sample_list)
    print(sorted_list)