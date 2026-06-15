class WordSorter:
    def sort(self, word_list):
        return sorted(word_list)
if __name__ == '__main__':
    sorter = WordSorter()
    words = ["banana", "apple", "cherry", "date", "elderberry"]
    sorted_words = sorter.sort(words)
    print(sorted_words)