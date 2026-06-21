class StringSorter:
    def __init__(self):
        self.sample_values = ["banana", "Apple", "cherry", "date"]

    def sort_strings_case_insensitive(self):
        return sorted(self.sample_values, key=lambda s: s.lower())

if __name__ == '__main__':
    sorter = StringSorter()
    result = sorter.sort_strings_case_insensitive()
    print(result)