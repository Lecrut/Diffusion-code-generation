class CaseInsensitiveSorter:
    DEFAULT_STRINGS = ['banana', 'Apple', 'cherry', 'date', 'Elderberry']

    @staticmethod
    def sort_alphabetically(strings):
        return sorted(strings, key=lambda s: s.lower())

    def __init__(self, strings=None):
        if strings is None:
            strings = CaseInsensitiveSorter.DEFAULT_STRINGS
        self.strings = strings

    def get_sorted_strings(self):
        return CaseInsensitiveSorter.sort_alphabetically(self.strings)

if __name__ == '__main__':
    sample_strings = ['grape', 'Orange', 'apple', 'Banana', 'cherry']
    sorter = CaseInsensitiveSorter(sample_strings)
    sorted_strings = sorter.get_sorted_strings()
    print(sorted_strings)