class StringSorter:
    def sort(self, word_list):
        return sorted(word_list)

if __name__ == '__main__':
    sorter = StringSorter()
    unsorted_words = ["banana", "apple", "cherry", "date", "elderberry"]
    sorted_words = sorter.sort(unsorted_words)
    print(sorted_words)