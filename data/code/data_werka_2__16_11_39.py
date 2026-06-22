class PositiveNumberFilter:
    @staticmethod
    def filter(numbers):
        return [num for num in numbers if num > 0]

if __name__ == '__main__':
    sample_values = [-5, -1, 2, 6, 0, -8, 4]
    positive_numbers = PositiveNumberFilter.filter(sample_values)
    print(positive_numbers)