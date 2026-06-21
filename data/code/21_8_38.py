class LexicalSorter:
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
    sample_strings = ['kiwi', 'Mango', 'apple', 'Orange', 'banana']
    sorter = LexicalSorter(sample_strings)
    sorter.display_sorted_strings()