class StringSorter:
    def __init__(self, strings):
        self.strings = strings

    def sorted_strings(self):
        return sorted(self.strings, key=lambda s: s.lower())

if __name__ == '__main__':
    sorter = StringSorter(["banana", "Apple", "cherry", "date"])
    sorted_list = sorter.sorted_strings()
    print(sorted_list)