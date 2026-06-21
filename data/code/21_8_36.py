class StringSorter:
    def __init__(self, strings):
        self.strings = strings

    def sort(self):
        return sorted(self.strings, key=lambda s: s.lower())

if __name__ == '__main__':
    sample_strings = ['banana', 'Apple', 'cherry', 'date', 'Elderberry']
    sorter = StringSorter(sample_strings)
    sorted_strings = sorter.sort()
    print(sorted_strings)