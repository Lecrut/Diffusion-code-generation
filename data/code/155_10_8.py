class SumCalculator:
    @staticmethod
    def calculate_list_sum(numbers):
        return sum(numbers)

if __name__ == '__main__':
    sample_values = [
        [1, 2, 3, 4, 5],
        [10.5, 20.5, 30.0],
        [-1, 5, -3, 10]
    ]
    for values in sample_values:
        result = SumCalculator.calculate_list_sum(values)
        print(result)