class AlphabeticalSorter:
    def sort_strings(self, strings):
        return sorted(strings, key=str.lower)

if __name__ == '__main__':
    sorter = AlphabeticalSorter()
    sample1 = ['banana', 'Apple', 'cherry', 'date']
    result1 = sorter.sort_strings(sample1)
    print(result1)
    
    sample2 = ['grape', 'orange', 'Mango', 'kiwi']
    result2 = sorter.sort_strings(sample2)
    print(result2)