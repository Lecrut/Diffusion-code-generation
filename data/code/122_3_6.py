import math

class AverageCalculator:
    @staticmethod
    def calculate_average(numbers):
        return math.fsum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [10.5, 20.5, 30.0, 40.0]
    print(AverageCalculator.calculate_average(sample_numbers))