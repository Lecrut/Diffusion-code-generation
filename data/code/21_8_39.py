class CaseInsensitiveSorter:
    def __init__(self, strings):
        if not isinstance(strings, list):
            raise ValueError("Input must be a list")
        if not all(isinstance(s, str) for s in strings):
            raise ValueError("All elements in the list must be strings")
        self.strings = strings

    def _validate_strings(self):
        for string in self.strings:
            if not isinstance(string, str):
                raise ValueError(f"Non-string element found: {string}")

    def sort(self):
        self._validate_strings()
        return sorted(self.strings, key=lambda s: s.lower())

if __name__ == '__main__':
    sample_strings = ['Lemon', 'apple', 'Orange', 'banana', 'Grape']
    sorter = CaseInsensitiveSorter(sample_strings)
    sorted_strings = sorter.sort()
    print(sorted_strings)