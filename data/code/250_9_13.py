import math

class MeanCalculator:
    @staticmethod
    def calculate_mean(numbers: list) -> float:
        if not numbers:
            return 0.0
        total_sum = math.fsum(numbers)
        count = len(numbers)
        return total_sum / count

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    mean_value = MeanCalculator.calculate_mean(sample_numbers)
    print(mean_value)