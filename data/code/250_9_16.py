import math

def calculate_mean(numbers: list) -> float:
    if not numbers:
        raise ValueError("The list of numbers cannot be empty.")
    total_sum = math.fsum(numbers)
    count = len(numbers)
    return total_sum / count

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    try:
        mean_value = calculate_mean(sample_numbers)
        print(mean_value)
    except ValueError as e:
        print(e)