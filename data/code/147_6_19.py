class NumericStringSorter:
    @staticmethod
    def sort(numeric_strings):
        return sorted(map(int, numeric_strings))

if __name__ == '__main__':
    sorter = NumericStringSorter()
    sample_values = ["3", "1", "4", "1", "5", "9"]
    print(sorter.sort(sample_values))