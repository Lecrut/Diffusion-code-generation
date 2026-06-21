from functools import reduce

class SumCalculator:
    @staticmethod
    def compute_total(numbers):
        return reduce(lambda x, y: x + y, numbers)

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    print(SumCalculator.compute_total(sample_numbers))