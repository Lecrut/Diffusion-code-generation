class CaseInsensitiveSorter:
    def __init__(self, strings):
        if not all(isinstance(s, str) for s in strings):
            raise ValueError("All elements must be strings")
        self.strings = strings

    def _sort_key(self, string):
        return string.lower()

    def sort(self):
        return sorted(self.strings, key=self._sort_key)

    def display_sorted_strings(self):
        sorted_strings = self.sort()
        print("Sorted Strings:")
        for string in sorted_strings:
            print(string)

if __name__ == '__main__':
    sample_strings = ['Pineapple', 'apple', 'Orange', 'banana', 'Grape']
    sorter = CaseInsensitiveSorter(sample_strings)
    sorter.display_sorted_strings()