class StringToIntegerSorter:
    @staticmethod
    def sort_numerical_strings(numerical_strings):
        return sorted(map(int, numerical_strings))

if __name__ == '__main__':
    sorter = StringToIntegerSorter()
    sample_values = ["3", "1", "4", "1", "5", "9"]
    sorted_numbers = sorter.sort_numerical_strings(sample_values)
    print(sorted_numbers)