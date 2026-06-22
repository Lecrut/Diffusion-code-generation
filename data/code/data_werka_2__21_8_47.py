class StringListSorter:
    def __init__(self, strings):
        if not all(isinstance(s, str) for s in strings):
            raise ValueError("All elements must be strings")
        self.strings = strings

    def _validate_strings(self):
        if not isinstance(self.strings, list):
            raise ValueError("Input must be a list of strings")
        if not all(isinstance(s, str) for s in self.strings):
            raise ValueError("All elements in the list must be strings")

    def sort_alphabetically(self):
        self._validate_strings()
        return sorted(self.strings, key=lambda s: s.lower())

if __name__ == '__main__':
    sample_strings = ['Pineapple', 'orange', 'Lemon', 'grape', 'Apple']
    sorter = StringListSorter(sample_strings)
    sorted_strings = sorter.sort_alphabetically()
    print(sorted_strings)