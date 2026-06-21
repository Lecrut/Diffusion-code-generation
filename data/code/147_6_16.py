class NumericStringSorter:
    @staticmethod
    def sort_numeric_strings(numeric_strings):
        return sorted(map(int, numeric_strings))

if __name__ == '__main__':
    sorter = NumericStringSorter()
    sample_values = ["3", "1", "4", "1", "5", "9"]
    print(sorter.sort_numeric_strings(sample_values))