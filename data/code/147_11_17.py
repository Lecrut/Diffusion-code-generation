class StringSorter:
    def sort_alphabetically(self, strings):
        return sorted(strings, key=str.lower)

if __name__ == '__main__':
    sorter = StringSorter()
    sample_strings_1 = ['banana', 'Apple', 'cherry', 'date']
    result_1 = sorter.sort_alphabetically(sample_strings_1)
    print(result_1)
    
    sample_strings_2 = ['Zebra', 'apple', 'Cherry', 'banana']
    result_2 = sorter.sort_alphabetically(sample_strings_2)
    print(result_2)