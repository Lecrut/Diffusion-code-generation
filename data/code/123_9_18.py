from functools import reduce

class SumCalculator:
    @staticmethod
    def calculate_sum(numbers):
        return reduce(lambda x, y: x + y, numbers)

if __name__ == '__main__':
    sample_values = [12, 18, 24, 30]
    calculator = SumCalculator()
    result = calculator.calculate_sum(sample_values)
    print(result)