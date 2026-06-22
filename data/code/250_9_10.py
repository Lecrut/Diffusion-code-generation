import math
MEAN_CALCULATION_PRECISION = 1e-09

def calculate_mean(numbers: list) -> float:
    total_sum = math.fsum(numbers)
    count = len(numbers)
    if count == 0:
        return 0.0
    mean_value = total_sum / count
    return round(mean_value, -int(math.floor(math.log10(abs(mean_value)) + MEAN_CALCULATION_PRECISION)))
if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    print(calculate_mean(sample_numbers))