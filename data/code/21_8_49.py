class CaseInsensitiveSorter:
    def __init__(self, strings):
        if not all(isinstance(s, str) for s in strings):
            raise ValueError("All elements must be strings")
        self.strings = strings

    def _sort_key(self, string):
        return string.lower()

    def sort(self):
        return sorted(self.strings, key=self._sort_key)

if __name__ == '__main__':
    sample_strings = ['Lemon', 'apple', 'Orange', 'Banana', 'grape']
    sorter = CaseInsensitiveSorter(sample_strings)
    sorted_strings = sorter.sort()
    print(sorted_strings)