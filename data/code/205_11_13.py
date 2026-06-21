class StringSorter:
    @staticmethod
    def sort_alphabetically(strings):
        return sorted(strings, key=lambda s: s.lower())

if __name__ == '__main__':
    sample_strings = ["banana", "Apple", "cherry", "date"]
    sorted_strings = StringSorter.sort_alphabetically(sample_strings)
    print(sorted_strings)