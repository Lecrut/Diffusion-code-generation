import math

def validate_numbers(numbers: list) -> bool:
    if not isinstance(numbers, list):
        return False
    if len(numbers) == 0:
        return False
    for num in numbers:
        if not isinstance(num, (int, float)):
            return False
    return True

def calculate_mean(numbers: list) -> float:
    if not validate_numbers(numbers):
        raise ValueError("Invalid input. Please provide a non-empty list of numbers.")
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