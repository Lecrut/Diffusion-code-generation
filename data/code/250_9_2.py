import math

def calculate_mean(numbers: list) -> float:
    return math.fsum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    print(calculate_mean(sample_numbers))