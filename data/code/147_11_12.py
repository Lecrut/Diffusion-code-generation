class StringSorter:
    def sort_alphabetically(self, strings):
        return sorted(strings, key=str.lower)

if __name__ == '__main__':
    sorter = StringSorter()
    sample_strings = ['banana', 'Apple', 'cherry', 'date']
    print(sorter.sort_alphabetically(sample_strings))