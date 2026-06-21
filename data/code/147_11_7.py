class AlphabeticalSorter:
    @staticmethod
    def sort_case_insensitive(strings):
        return sorted(strings, key=str.lower)

if __name__ == '__main__':
    sorter = AlphabeticalSorter()
    sample_strings = ['banana', 'Apple', 'cherry', 'date']
    sorted_strings = sorter.sort_case_insensitive(sample_strings)
    print(sorted_strings)