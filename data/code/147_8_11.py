class StringSorter:
    def __init__(self, strings):
        self.strings = strings

    def sort_case_insensitive(self):
        return sorted(self.strings, key=lambda s: s.lower())

if __name__ == '__main__':
    sorter = StringSorter(["banana", "Apple", "cherry", "date"])
    sorted_strings = sorter.sort_case_insensitive()
    print(sorted_strings)