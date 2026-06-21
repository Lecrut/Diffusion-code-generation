class NumberSorter:
    @staticmethod
    def sort_mixed_numbers(numbers):
        return sorted(map(float, numbers))

if __name__ == '__main__':
    sample_values = ['3.5', 2, '4', 1.1]
    sorter = NumberSorter()
    print(sorter.sort_mixed_numbers(sample_values))