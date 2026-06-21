class StringSorter:
    def __init__(self, strings):
        self.strings = strings

    def sort_in_place(self):
        n = len(self.strings)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if self.strings[j] < self.strings[min_idx]:
                    min_idx = j
            self.strings[i], self.strings[min_idx] = self.strings[min_idx], self.strings[i]

if __name__ == '__main__':
    sorter = StringSorter(["banana", "apple", "cherry", "date"])
    sorter.sort_in_place()
    print(sorter.strings)