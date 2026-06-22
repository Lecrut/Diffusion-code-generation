class CaseInsensitiveSorter:
    def __init__(self, strings):
        self._validate_input(strings)
        self.strings = strings

    def _validate_input(self, strings):
        if not all(isinstance(s, str) for s in strings):
            raise ValueError("All elements must be strings")

    def sort(self):
        return sorted(self.strings, key=lambda s: s.lower())

    def display_sorted_strings(self):
        sorted_strings = self.sort()
        print("Sorted Strings:")
        for string in sorted_strings:
            print(string)

if __name__ == '__main__':
    sample_strings = ['Lemon', 'lime', 'Apple', 'banana', 'Cherry']
    sorter = CaseInsensitiveSorter(sample_strings)
    sorter.display_sorted_strings()