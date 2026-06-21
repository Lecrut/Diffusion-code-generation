class StringSorter:
    def sort_strings_case_insensitive(self, strings):
        return sorted(strings, key=lambda s: s.lower())

if __name__ == '__main__':
    sorter = StringSorter()
    sample_values = ["banana", "Apple", "cherry", "date"]
    sorted_values = sorter.sort_strings_case_insensitive(sample_values)
    print(sorted_values)