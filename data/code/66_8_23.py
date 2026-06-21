class NumberComparator:
    @staticmethod
    def compare_adjacent(numbers):
        return [numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1)]

if __name__ == '__main__':
    sample_values = [7, 3, 5, 9, 2, 6]
    result = NumberComparator.compare_adjacent(sample_values)
    print(result)