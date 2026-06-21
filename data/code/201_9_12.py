from functools import reduce
import operator

class AverageCalculator:
    @staticmethod
    def calculate_average(numbers):
        if not numbers:
            return 0
        total = reduce(operator.add, numbers)
        average = total / len(numbers)
        return average

if __name__ == '__main__':
    calculator = AverageCalculator()
    sample_numbers = [10, 20, 30, 40, 50]
    print(calculator.calculate_average(sample_numbers))