import math

class Statistics:
    @staticmethod
    def calculate_mean(numbers: list) -> float:
        total_sum = math.fsum(numbers)
        count = len(numbers)
        return total_sum / count if count > 0 else 0.0

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    mean_value = Statistics.calculate_mean(sample_numbers)
    print(mean_value)