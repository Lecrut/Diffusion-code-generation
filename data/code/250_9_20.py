import math

def calculate_mean(numbers: list[float]) -> float:
    return math.fsum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [1.5, 2.5, 3.5, 4.5]
    print(calculate_mean(sample_numbers))