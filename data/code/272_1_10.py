class AlphabeticalSorter:
    def __init__(self, word_list):
        self.word_list = word_list

    def sort(self):
        return sorted(self.word_list)

if __name__ == '__main__':
    sorter = AlphabeticalSorter(["banana", "apple", "cherry", "date"])
    sorted_result = sorter.sort()
    print(sorted_result)