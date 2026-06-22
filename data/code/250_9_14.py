import math
SAMPLE_SIZE = 5

def calculate_mean(numbers: list) -> float:
    if not numbers:
        return 0.0
    total_sum = math.fsum(numbers)
    count = len(numbers)
    return total_sum / count
if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50][:SAMPLE_SIZE]
    mean_value = calculate_mean(sample_numbers)
    print(f'The mean of {sample_numbers} is: {mean_value}')