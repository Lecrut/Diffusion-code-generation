class AlphabeticalSorter:
    def __init__(self, strings):
        if not all(isinstance(s, str) for s in strings):
            raise ValueError("All elements must be strings")
        self.strings = strings

    def sort(self):
        return sorted(self.strings, key=lambda s: s.lower())

if __name__ == '__main__':
    sample_strings = ['grape', 'Orange', 'apple', 'Banana', 'cherry']
    sorter = AlphabeticalSorter(sample_strings)
    sorted_strings = sorter.sort()
    print(sorted_strings)