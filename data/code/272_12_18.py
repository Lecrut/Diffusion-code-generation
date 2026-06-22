class AlphabeticalSorter:
    @staticmethod
    def sort_words(word_list):
        return sorted(word_list)

if __name__ == '__main__':
    sorter = AlphabeticalSorter()
    words = ["banana", "apple", "zebra", "cat", "dog"]
    sorted_words = sorter.sort_words(words)
    print(sorted_words)