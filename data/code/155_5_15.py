from functools import reduce
import operator

class SumCalculator:
    @staticmethod
    def calculate_sum(data):
        return reduce(operator.add, data)

if __name__ == '__main__':
    sample_numbers = [12345678901234567890, 98765432109876543210, 11111111111111111111]
    calculator = SumCalculator()
    result = calculator.calculate_sum(sample_numbers)
    print(result)