class LengthSorter:
    def __init__(self, string_set):
        self.string_set = string_set

    def get_unique_lengths(self):
        return sorted({len(s) for s in self.string_set})

if __name__ == '__main__':
    sorter = LengthSorter({"apple", "banana", "cherry", "date"})
    print(sorter.get_unique_lengths())