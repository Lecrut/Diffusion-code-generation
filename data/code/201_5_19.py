from math import fsum

def calculate_average(numbers: list[float]) -> float:
    return fsum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = [3.5, 2.1, 4.8, 5.6]
    print(calculate_average(sample_values))