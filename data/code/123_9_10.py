from functools import reduce

class SumCalculator:

    @staticmethod
    def calculate_sum(numbers):
        return reduce(lambda x, y: x + y, numbers)
if __name__ == '__main__':
    calculator = SumCalculator()
    sample_values_1 = [1, 2, 3, 4, 5]
    sample_values_2 = [10, 20, 30, 40, 50]
    result_1 = calculator.calculate_sum(sample_values_1)
    result_2 = calculator.calculate_sum(sample_values_2)
    print(result_1)
    print(result_2)