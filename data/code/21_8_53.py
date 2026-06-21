class CaseInsensitiveSorter:
    def __init__(self, strings):
        if not all(isinstance(s, str) for s in strings):
            raise ValueError("All elements must be strings")
        self.strings = strings

    def sort(self):
        return sorted(self.strings, key=str.lower)

    def display_sorted_strings(self):
        sorted_strings = self.sort()
        print(*sorted_strings, sep='\n')

if __name__ == '__main__':
    sample_strings = ['Lemon', 'lime', 'Apple', 'orange', 'Banana']
    sorter = CaseInsensitiveSorter(sample_strings)
    sorter.display_sorted_strings()