import math

def calculate_mean(numbers: list) -> float:
    if not numbers:
        raise ValueError("The input list cannot be empty")
    return math.fsum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    try:
        print(calculate_mean(sample_numbers))
    except ValueError as e:
        print(e)