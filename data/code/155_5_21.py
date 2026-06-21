from functools import reduce
import operator

class SumCalculator:
    @staticmethod
    def sum_large_integers(numbers):
        return reduce(operator.add, numbers)

if __name__ == '__main__':
    sample_numbers = [12345678901234567890, 98765432109876543210, 11111111111111111111]
    calculator = SumCalculator()
    result = calculator.sum_large_integers(sample_numbers)
    print(result)