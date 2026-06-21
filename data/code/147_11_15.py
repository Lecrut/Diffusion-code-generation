class AlphabeticalSorter:
    def sort(self, input_list):
        return sorted(input_list, key=str.lower)

if __name__ == '__main__':
    sorter = AlphabeticalSorter()
    sample_values_1 = ['banana', 'Apple', 'cherry', 'date']
    print(sorter.sort(sample_values_1))
    
    sample_values_2 = ["grape", "Orange", "apple", "Cherry"]
    print(sorter.sort(sample_values_2))