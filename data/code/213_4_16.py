class DescendingSorter:
    @staticmethod
    def sort_numbers(numbers):
        numbers.sort(key=lambda x: -x)
        return numbers

if __name__ == '__main__':
    sample_values = [3.5, 1.2, 4.8, 2.9, 0.7]
    sorted_values = DescendingSorter.sort_numbers(sample_values)
    print(sorted_values)