from functools import reduce

class SumCalculator:
    @staticmethod
    def sum_numbers(numbers):
        return reduce(lambda x, y: x + y, numbers)

if __name__ == '__main__':
    calculator = SumCalculator()
    sample_values1 = [1, 2, 3, 4, 5]
    sample_values2 = [10, 20, 30, 40, 50]
    
    result1 = calculator.sum_numbers(sample_values1)
    result2 = calculator.sum_numbers(sample_values2)
    
    print(result1)
    print(result2)