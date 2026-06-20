import math

class AverageCalculator:
    @staticmethod
    def calculate_average(numbers):
        return math.fsum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [12.5, 23.75, 34.0, 45.25]
    print(AverageCalculator.calculate_average(sample_numbers))