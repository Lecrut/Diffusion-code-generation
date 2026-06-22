class WordSorter:
    @staticmethod
    def sort(word_list):
        return sorted(word_list)

if __name__ == '__main__':
    sorter = WordSorter()
    words = ["banana", "apple", "zebra", "cat", "dog"]
    sorted_words = sorter.sort(words)
    print(sorted_words)