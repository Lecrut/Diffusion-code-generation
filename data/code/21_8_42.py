class CaseInsensitiveSorter:
    def __init__(self, strings):
        self.strings = strings

    def sort(self):
        return sorted(self.strings, key=lambda s: s.lower())

    def display_sorted_strings(self):
        sorted_strings = self.sort()
        print("Sorted Strings:")
        for string in sorted_strings:
            print(string)

if __name__ == '__main__':
    sample_strings = ['Blueberry', 'apple', 'Cherry', 'date', 'Elderberry']
    sorter = CaseInsensitiveSorter(sample_strings)
    sorted_list = sorter.sort()
    print("Sorted List:", sorted_list)
    sorter.display_sorted_strings()