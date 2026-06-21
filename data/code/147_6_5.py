class NumericStringSorter:
    def __init__(self, numeric_strings):
        self.numeric_strings = numeric_strings

    def sort(self):
        return sorted(map(int, self.numeric_strings))

if __name__ == '__main__':
    sorter = NumericStringSorter(["3", "1", "4", "1", "5", "9"])
    print(sorter.sort())