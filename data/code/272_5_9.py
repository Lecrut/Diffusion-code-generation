class WordSorter:
    def __init__(self, word_list):
        self.word_list = word_list

    def reverse_alphabetical_sort(self):
        return sorted(self.word_list, reverse=True)

if __name__ == '__main__':
    sorter = WordSorter(["banana", "apple", "cherry", "date"])
    print(sorter.reverse_alphabetical_sort())