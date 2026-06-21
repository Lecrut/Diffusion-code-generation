class StringSorter:
    @staticmethod
    def sort_alphabetically(strings):
        return sorted(strings, key=lambda s: s.lower())

if __name__ == '__main__':
    sample_values = ["banana", "Apple", "cherry", "date"]
    sorter = StringSorter()
    sorted_values = sorter.sort_alphabetically(sample_values)
    print(sorted_values)