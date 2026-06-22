class CaseInsensitiveSorter:
    def __init__(self, strings):
        if not all(isinstance(s, str) for s in strings):
            raise ValueError("All elements must be strings")
        self.strings = strings

    def _validate_strings(self):
        return all(isinstance(s, str) for s in self.strings)

    def sort(self):
        if not self._validate_strings():
            raise ValueError("All elements must be strings")
        return sorted(self.strings, key=lambda s: s.lower())

if __name__ == '__main__':
    sample_strings = ['Lemon', 'lime', 'Apple', 'Orange', 'banana']
    sorter = CaseInsensitiveSorter(sample_strings)
    sorted_strings = sorter.sort()
    print(sorted_strings)