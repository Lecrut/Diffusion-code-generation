class NumberSorter:
    @staticmethod
    def sort_descending(numbers):
        numbers.sort(key=lambda x: -x)
        return numbers

if __name__ == '__main__':
    sample_values = [3.5, 1.2, 4.8, 2.9, 0.7]
    sorter = NumberSorter()
    sorted_values = sorter.sort_descending(sample_values)
    print(sorted_values)