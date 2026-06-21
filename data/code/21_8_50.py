class CaseInsensitiveSorter:
    def __init__(self, strings):
        self.strings = strings

    def sort(self):
        return sorted(self.strings, key=lambda s: s.lower())

    def get_sorted_strings(self):
        return self.sort()

if __name__ == '__main__':
    sample_strings = ['banana', 'Apple', 'cherry', 'date', 'Elderberry']
    sorter = CaseInsensitiveSorter(sample_strings)
    print("Sorted Strings:", sorter.get_sorted_strings())