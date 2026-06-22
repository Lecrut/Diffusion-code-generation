import math

def calculate_mean(numbers: list) -> float:
    if not numbers:
        return 0.0
    total_sum = math.fsum(numbers)
    count = len(numbers)
    return total_sum / count

if __name__ == '__main__':
    sample_numbers = [12, 24, 36, 48, 60]
    print(calculate_mean(sample_numbers))